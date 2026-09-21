import os
import logging
from functools import wraps
import numpy as np
import pandas as pd
import requests
import joblib
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, render_template, request, jsonify,
    flash, redirect, url_for, session
)
import tensorflow as tf
from tensorflow import keras

from destinations_data import DESTINATIONS_DATA

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env if present
load_dotenv()
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "").strip()

# Initialize Flask App
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "ai-travel-recommender-deeplearning-secret-key-2026")

# In-Memory / Preloaded User Database with Demo Credentials
USERS_DB = {
    "traveler@ai.com": {
        "name": "Demo Traveler",
        "email": "traveler@ai.com",
        "password": generate_password_hash("password123")
    },
    "admin@travel.ai": {
        "name": "Admin Explorer",
        "email": "admin@travel.ai",
        "password": generate_password_hash("admin123")
    }
}

# Global variables for model and preprocessors
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "recommender.keras")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")
ENCODERS_PATH = os.path.join(BASE_DIR, "model", "encoders.pkl")

model = None
scaler = None
encoders_dict = None
onehot_encoder = None
label_encoder = None

def load_ai_artifacts():
    """Loads the trained Keras neural network and preprocessing objects once on startup."""
    global model, scaler, encoders_dict, onehot_encoder, label_encoder
    
    logger.info("Loading Deep Learning model and preprocessors...")
    
    if not os.path.exists(MODEL_PATH):
        logger.error(f"Trained model not found at {MODEL_PATH}. Please run model/train.py first.")
        return False
        
    if not os.path.exists(SCALER_PATH) or not os.path.exists(ENCODERS_PATH):
        logger.error("Preprocessing objects (scaler.pkl, encoders.pkl) missing.")
        return False

    try:
        model = keras.models.load_model(MODEL_PATH)
        logger.info(f"Keras model loaded successfully from {MODEL_PATH}.")
        
        scaler = joblib.load(SCALER_PATH)
        encoders_dict = joblib.load(ENCODERS_PATH)
        onehot_encoder = encoders_dict["onehot_encoder"]
        label_encoder = encoders_dict["label_encoder"]
        
        logger.info(f"Loaded scaler and encoders for {len(label_encoder.classes_)} destinations.")
        return True
    except Exception as e:
        logger.exception(f"Error loading AI artifacts: {e}")
        return False

# Initialize artifacts on startup
artifacts_loaded = load_ai_artifacts()

def login_required(f):
    """Decorator to require user authentication for protected routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_email" not in session:
            flash("Please sign in with your credentials to access the travel recommender.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

def fetch_unsplash_image(destination_name, search_query=None):
    """
    Fetches dynamic destination image from Unsplash API.
    Falls back gracefully to curated high-resolution photography with attribution.
    """
    dest_info = DESTINATIONS_DATA.get(destination_name, {})
    fallback = dest_info.get("fallback_image", {
        "url": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Unsplash Travel",
        "photographer_url": "https://unsplash.com"
    })
    
    if not UNSPLASH_ACCESS_KEY:
        logger.info(f"No UNSPLASH_ACCESS_KEY configured. Using curated fallback for {destination_name}.")
        return fallback

    query = search_query or dest_info.get("search_query", f"{destination_name} India travel landscape")
    endpoint = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "orientation": "landscape",
        "per_page": 1,
        "client_id": UNSPLASH_ACCESS_KEY
    }

    try:
        response = requests.get(endpoint, params=params, timeout=4)
        if response.status_code == 200:
            data = response.json()
            if data.get("results") and len(data["results"]) > 0:
                photo = data["results"][0]
                return {
                    "url": photo["urls"]["regular"],
                    "photographer": photo["user"]["name"],
                    "photographer_url": photo["user"]["links"]["html"] + "?utm_source=ai_travel_recommender&utm_medium=referral"
                }
    except Exception as e:
        logger.warning(f"Unsplash API call failed ({e}). Using curated fallback.")
        
    return fallback

def preprocess_user_input(user_data):
    """Preprocesses user preferences matching the exact training pipeline."""
    duration = float(user_data["duration"])
    df_num = pd.DataFrame({"Duration": [duration]})
    df_cat = pd.DataFrame([{
        "Budget": user_data["budget"],
        "Season": user_data["season"],
        "Travel_Type": user_data["travel_type"],
        "Travel_Preference": user_data["travel_preference"],
        "Region": user_data["region"]
    }])
    
    X_num = scaler.transform(df_num)
    X_cat = onehot_encoder.transform(df_cat)
    return np.hstack([X_num, X_cat])

# =====================================================================
# Authentication Routes
# =====================================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles user sign in and displays quick demo credentials."""
    if "user_email" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        user = USERS_DB.get(email)
        if user and check_password_hash(user["password"], password):
            session["user_email"] = user["email"]
            session["user_name"] = user["name"]
            flash(f"Welcome back, {user['name']}! Ready to discover your next destination?", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password. Please use the demo credentials provided.", "error")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles new user registration."""
    if "user_email" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("Please fill in all registration fields.", "error")
            return render_template("register.html")

        if email in USERS_DB:
            flash("An account with this email already exists. Please sign in.", "error")
            return redirect(url_for("login"))

        USERS_DB[email] = {
            "name": name,
            "email": email,
            "password": generate_password_hash(password)
        }
        flash("Registration successful! You can now log in with your credentials.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
def logout():
    """Logs out user and clears session."""
    session.clear()
    flash("You have been signed out successfully.", "info")
    return redirect(url_for("login"))

# =====================================================================
# Main Application Routes (Protected)
# =====================================================================

@app.route("/", methods=["GET"])
@login_required
def home():
    """Renders the interactive AI Travel Recommender home page."""
    current_user = {
        "name": session.get("user_name", "Traveler"),
        "email": session.get("user_email", "")
    }
    return render_template("index.html", user=current_user)

@app.route("/recommend", methods=["POST"])
@login_required
def recommend():
    """Handles travel recommendation requests using the Deep Learning model."""
    global artifacts_loaded
    if not artifacts_loaded:
        artifacts_loaded = load_ai_artifacts()
        if not artifacts_loaded:
            flash("Deep Learning model is currently unavailable. Please ensure model/train.py has been executed.", "error")
            return redirect(url_for("home"))

    try:
        budget = request.form.get("budget", "").strip()
        duration_str = request.form.get("duration", "").strip()
        season = request.form.get("season", "").strip()
        travel_type = request.form.get("travel_type", "").strip()
        travel_preference = request.form.get("travel_preference", "").strip()
        region = request.form.get("region", "").strip()

        if not all([budget, duration_str, season, travel_type, travel_preference, region]):
            flash("Please fill in all travel preference fields to get an accurate recommendation.", "error")
            return redirect(url_for("home"))

        try:
            duration = int(duration_str)
            if duration < 1 or duration > 60:
                flash("Duration must be a realistic number of days between 1 and 60.", "error")
                return redirect(url_for("home"))
        except ValueError:
            flash("Invalid duration entered. Please enter a valid whole number of days.", "error")
            return redirect(url_for("home"))

        user_data = {
            "budget": budget,
            "duration": duration,
            "season": season,
            "travel_type": travel_type,
            "travel_preference": travel_preference,
            "region": region
        }

        # Preprocess input matching training pipeline
        X_input = preprocess_user_input(user_data)

        # Deep Learning Softmax Predictions
        prediction_probs = model.predict(X_input, verbose=0)[0]
        
        # Primary Prediction
        top_idx = int(np.argmax(prediction_probs))
        destination_name = str(label_encoder.classes_[top_idx])
        top_confidence = float(prediction_probs[top_idx]) * 100.0

        # Top 3 Alternative Recommendations
        sorted_indices = np.argsort(prediction_probs)[::-1]
        top_alternatives = []
        for idx in sorted_indices[1:4]:
            alt_name = str(label_encoder.classes_[idx])
            alt_prob = float(prediction_probs[idx]) * 100.0
            alt_info = DESTINATIONS_DATA.get(alt_name, {})
            top_alternatives.append({
                "name": alt_name,
                "confidence": round(alt_prob, 1),
                "region": alt_info.get("region", ""),
                "tagline": alt_info.get("tagline", ""),
                "image": alt_info.get("fallback_image", {}).get("url", "")
            })

        # Destination Knowledge Metadata
        dest_metadata = DESTINATIONS_DATA.get(destination_name, {
            "name": destination_name,
            "state": "Incredible India",
            "region": region,
            "tagline": "A Wonderful Destination to Explore",
            "description": f"{destination_name} is an exceptional destination that aligns with your {travel_preference.lower()} preferences and {season.lower()} travel plans.",
            "best_time_to_visit": f"Ideal during {season}",
            "season_suitability": season,
            "climate_type": "Varied",
            "budget_level": budget,
            "ideal_duration": f"{duration} Days",
            "recommended_activities": [
                f"Sightseeing & scenic exploration in {destination_name}",
                f"Experiencing local cultural heritage and cuisine",
                f"Adventure and nature walks suited for {travel_type.lower()} travelers"
            ],
            "top_attractions": [f"{destination_name} City Center", "Scenic Viewpoint", "Heritage Monument"]
        })

        # Dynamic Visual
        image_data = fetch_unsplash_image(destination_name, dest_metadata.get("search_query"))

        current_user = {
            "name": session.get("user_name", "Traveler"),
            "email": session.get("user_email", "")
        }

        return render_template(
            "results.html",
            destination=destination_name,
            confidence=round(top_confidence, 1),
            metadata=dest_metadata,
            image=image_data,
            user_input=user_data,
            alternatives=top_alternatives,
            user=current_user
        )

    except Exception as e:
        logger.exception(f"Unexpected error during recommendation: {e}")
        flash(f"An unexpected error occurred while processing your request: {str(e)}", "error")
        return redirect(url_for("home"))

@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    """JSON API endpoint for programmatic deep learning recommendations."""
    global artifacts_loaded
    if not artifacts_loaded:
        artifacts_loaded = load_ai_artifacts()
        if not artifacts_loaded:
            return jsonify({"status": "error", "message": "Deep Learning model artifacts not loaded."}), 503

    try:
        data = request.get_json(force=True)
        required_keys = ["budget", "duration", "season", "travel_type", "travel_preference", "region"]
        for key in required_keys:
            if key not in data:
                return jsonify({"status": "error", "message": f"Missing required parameter: {key}"}), 400

        X_input = preprocess_user_input(data)
        prediction_probs = model.predict(X_input, verbose=0)[0]
        
        top_idx = int(np.argmax(prediction_probs))
        destination_name = str(label_encoder.classes_[top_idx])
        top_confidence = float(prediction_probs[top_idx]) * 100.0

        dest_metadata = DESTINATIONS_DATA.get(destination_name, {})
        image_data = fetch_unsplash_image(destination_name, dest_metadata.get("search_query"))

        return jsonify({
            "status": "success",
            "recommended_destination": destination_name,
            "confidence_percentage": round(top_confidence, 2),
            "destination_metadata": dest_metadata,
            "image": image_data,
            "all_probabilities": {
                str(label_encoder.classes_[i]): round(float(prediction_probs[i]) * 100.0, 2)
                for i in range(len(label_encoder.classes_))
            }
        })
    except Exception as e:
        logger.exception(f"API Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("login.html", error="The requested page was not found."), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("login.html", error="An internal server error occurred. Please try again."), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "127.0.0.1")
    logger.info(f"Starting AI Travel Recommender Web Application on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
