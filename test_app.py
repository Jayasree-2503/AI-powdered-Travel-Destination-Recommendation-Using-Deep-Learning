"""
End-to-end verification and testing suite for AI Travel Destination Recommender.
Tests authentication, login, demo credentials, protected routes, deep learning inference,
Flask endpoints, and response structure.
"""

import os
import unittest
import json
import numpy as np
from app import app, load_ai_artifacts, preprocess_user_input, model, label_encoder

class TravelRecommenderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n" + "=" * 60)
        print("Running AI Travel Recommender Verification Tests")
        print("=" * 60)
        cls.client = app.test_client()
        app.config['TESTING'] = True
        cls.loaded = load_ai_artifacts()
        if not cls.loaded:
            raise RuntimeError("Failed to load AI model artifacts during test setup.")

    def test_01_artifacts_loaded(self):
        """Verify model, scaler, and encoders are loaded correctly."""
        self.assertTrue(self.loaded)
        self.assertIsNotNone(model)
        self.assertEqual(len(label_encoder.classes_), 15)
        print(" Artifacts Loaded Successfully (15 Destinations).")

    def test_02_unauthenticated_redirect(self):
        """Verify unauthenticated user accessing / is redirected to /login."""
        response = self.client.get("/", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.headers["Location"])
        print(" Unauthenticated access to / redirected to /login as expected.")

    def test_03_login_page(self):
        """Test GET /login displays clean login form and branding."""
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome Back", response.data)
        self.assertIn(b"Sign in to your account to continue", response.data)
        self.assertIn(b"Email Address", response.data)
        self.assertIn(b"Password", response.data)
        self.assertIn(b"Sign In", response.data)
        print(" Login page renders with clean standard sign-in form.")

    def test_04_user_authentication_flow(self):
        """Test login with demo credentials, protected access, and logout."""
        # 1. Login with demo credentials
        login_res = self.client.post("/login", data={
            "email": "traveler@ai.com",
            "password": "password123"
        }, follow_redirects=True)
        self.assertEqual(login_res.status_code, 200)
        self.assertIn(b"Demo Traveler", login_res.data)
        self.assertIn(b"Define Your Journey", login_res.data)
        print(" Login with demo credentials successful.")

        # 2. Access protected recommendation route
        payload = {
            "budget": "Medium",
            "duration": "6",
            "season": "Winter",
            "travel_type": "Friends",
            "travel_preference": "Mountains",
            "region": "North India"
        }
        rec_res = self.client.post("/recommend", data=payload, follow_redirects=True)
        self.assertEqual(rec_res.status_code, 200)
        self.assertIn(b"YOUR RECOMMENDED DESTINATION", rec_res.data)
        self.assertIn(b"MANALI", rec_res.data)
        print(" Authenticated recommendation for Manali successful.")

        # 3. Logout
        logout_res = self.client.get("/logout", follow_redirects=True)
        self.assertEqual(logout_res.status_code, 200)
        self.assertIn(b"You have been signed out successfully", logout_res.data)
        print(" Logout and session clearance successful.")

    def test_05_inference_predictions(self):
        """Test Deep Learning predictions for various travel personas."""
        test_cases = [
            {
                "input": {"budget": "Medium", "duration": 6, "season": "Winter", "travel_type": "Friends", "travel_preference": "Mountains", "region": "North India"},
                "expected": "Manali"
            },
            {
                "input": {"budget": "High", "duration": 5, "season": "Winter", "travel_type": "Friends", "travel_preference": "Beach", "region": "West India"},
                "expected": "Goa"
            },
            {
                "input": {"budget": "Low", "duration": 3, "season": "Winter", "travel_type": "Solo", "travel_preference": "Spiritual", "region": "North India"},
                "expected": "Varanasi"
            },
            {
                "input": {"budget": "High", "duration": 8, "season": "Winter", "travel_type": "Couple", "travel_preference": "Beach", "region": "South India"},
                "expected": "Andaman"
            },
            {
                "input": {"budget": "Low", "duration": 3, "season": "Monsoon", "travel_type": "Family", "travel_preference": "Nature", "region": "South India"},
                "expected": "Araku Valley"
            },
            {
                "input": {"budget": "Medium", "duration": 4, "season": "Summer", "travel_type": "Family", "travel_preference": "Mountains", "region": "South India"},
                "expected": "Ooty"
            },
            {
                "input": {"budget": "High", "duration": 7, "season": "Summer", "travel_type": "Couple", "travel_preference": "Mountains", "region": "North India"},
                "expected": "Kashmir"
            },
            {
                "input": {"budget": "Low", "duration": 4, "season": "Spring", "travel_type": "Solo", "travel_preference": "Adventure", "region": "North India"},
                "expected": "Rishikesh"
            }
        ]

        for tc in test_cases:
            X = preprocess_user_input(tc["input"])
            probs = model.predict(X, verbose=0)[0]
            top_dest = label_encoder.classes_[np.argmax(probs)]
            conf = float(np.max(probs)) * 100.0
            print(f" Tested {tc['input']['travel_preference']} in {tc['input']['region']} -> Predicted: {top_dest} ({conf:.1f}% confidence) | Expected: {tc['expected']}")
            self.assertEqual(top_dest, tc["expected"])
            self.assertGreater(conf, 50.0)

    def test_06_api_recommend_json(self):
        """Test POST /api/recommend returns valid JSON with probability distribution."""
        payload = {
            "budget": "High",
            "duration": 5,
            "season": "Winter",
            "travel_type": "Couple",
            "travel_preference": "Beach",
            "region": "West India"
        }
        response = self.client.post(
            "/api/recommend",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["recommended_destination"], "Goa")
        self.assertIn("confidence_percentage", data)
        self.assertIn("all_probabilities", data)
        self.assertEqual(len(data["all_probabilities"]), 15)
        print(f" REST API POST /api/recommend verified: {data['recommended_destination']} ({data['confidence_percentage']}%)")

    def test_07_registration_flow(self):
        """Test new user registration."""
        reg_res = self.client.post("/register", data={
            "name": "Sarah Connor",
            "email": "sarah@travel.ai",
            "password": "securepassword"
        }, follow_redirects=True)
        self.assertEqual(reg_res.status_code, 200)
        self.assertIn(b"Registration successful", reg_res.data)
        print(" User registration verified.")

if __name__ == "__main__":
    unittest.main()
