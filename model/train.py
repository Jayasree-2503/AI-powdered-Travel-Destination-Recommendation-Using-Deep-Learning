import os
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import tensorflow as tf
from tensorflow import keras
from keras import layers, callbacks

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

def train_model():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, "dataset", "travel_dataset.csv")
    model_dir = os.path.join(base_dir, "model")
    static_img_dir = os.path.join(base_dir, "static", "images")
    os.makedirs(model_dir, exist_ok=True)
    os.makedirs(static_img_dir, exist_ok=True)

    print("=" * 60)
    print("AI Travel Destination Recommender - Training Pipeline")
    print("=" * 60)

    # 1. Load Dataset
    print("\n[Step 1] Loading Dataset...")
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at {dataset_path}. Please run generate_dataset.py first.")
    
    df = pd.read_csv(dataset_path)
    print(f"Loaded {len(df)} samples with columns: {list(df.columns)}")
    print(f"Total Destinations: {df['Destination'].nunique()}")

    # 2. Check for missing values
    print("\n[Step 2] Checking for missing values...")
    missing = df.isnull().sum()
    print("Missing values per column:\n", missing)
    if missing.any():
        print("Handling missing values (dropping rows with nulls)...")
        df = df.dropna().reset_index(drop=True)

    # 3. Categorical and Numerical Feature Definitions
    cat_features = ["Budget", "Season", "Travel_Type", "Travel_Preference", "Region"]
    num_features = ["Duration"]
    target_col = "Destination"

    # 4. Encoders & Scalers
    print("\n[Step 3] Preprocessing Features and Target...")
    
    # Target Encoding
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(df[target_col])
    num_classes = len(label_encoder.classes_)
    print(f"Encoded {num_classes} destination classes: {list(label_encoder.classes_)}")

    # Categorical Feature Encoding
    onehot_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    X_cat = onehot_encoder.fit_transform(df[cat_features])
    cat_feature_names = onehot_encoder.get_feature_names_out(cat_features)
    print(f"Categorical features transformed into {X_cat.shape[1]} one-hot dimensions.")

    # Numerical Feature Scaling
    scaler = StandardScaler()
    X_num = scaler.fit_transform(df[num_features])
    print(f"Numerical feature 'Duration' scaled (Mean: {scaler.mean_[0]:.2f}, Std: {scaler.scale_[0]:.2f}).")

    # Combine Features
    X = np.hstack([X_num, X_cat])
    feature_names = num_features + list(cat_feature_names)
    print(f"Final Input Feature Matrix shape: {X.shape}")

    # Save preprocessing objects
    scaler_path = os.path.join(model_dir, "scaler.pkl")
    encoders_path = os.path.join(model_dir, "encoders.pkl")

    joblib.dump(scaler, scaler_path)
    joblib.dump({
        "onehot_encoder": onehot_encoder,
        "label_encoder": label_encoder,
        "cat_features": cat_features,
        "num_features": num_features,
        "feature_names": feature_names,
        "destinations": list(label_encoder.classes_),
        "num_classes": num_classes
    }, encoders_path)
    print(f"Saved preprocessing objects to:\n - {scaler_path}\n - {encoders_path}")

    # 5. Split Data into Train, Validation, and Test Sets
    print("\n[Step 4] Splitting Dataset (80% Train, 20% Test)...")
    X_train_full, X_test, y_train_full, y_test = train_test_split(
        X, y_encoded, test_size=0.20, random_state=42, stratify=y_encoded
    )
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_full, y_train_full, test_size=0.15, random_state=42, stratify=y_train_full
    )
    print(f"Train Set: {X_train.shape[0]} samples")
    print(f"Validation Set: {X_val.shape[0]} samples")
    print(f"Test Set: {X_test.shape[0]} samples")

    # 6. Deep Learning Model Architecture
    print("\n[Step 5] Building TensorFlow/Keras Feedforward Neural Network...")
    input_dim = X.shape[1]
    
    model = keras.Sequential([
        keras.Input(shape=(input_dim,)),
        layers.Dense(128, activation="relu", name="dense_128"),
        layers.BatchNormalization(name="batch_norm_1"),
        layers.Dropout(0.3, name="dropout_1"),
        layers.Dense(64, activation="relu", name="dense_64"),
        layers.Dropout(0.2, name="dropout_2"),
        layers.Dense(32, activation="relu", name="dense_32"),
        layers.Dense(num_classes, activation="softmax", name="output_softmax")
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    
    model.summary()

    # 7. Model Training Callbacks
    early_stopping = callbacks.EarlyStopping(
        monitor="val_loss",
        patience=20,
        restore_best_weights=True,
        verbose=1
    )
    
    reduce_lr = callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=6,
        min_lr=1e-5,
        verbose=1
    )

    # 8. Train the Deep Learning Model
    print("\n[Step 6] Training Neural Network...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=100,
        batch_size=32,
        callbacks=[early_stopping, reduce_lr],
        verbose=1
    )

    # 9. Save Trained Model
    model_save_path = os.path.join(model_dir, "recommender.keras")
    model.save(model_save_path)
    print(f"\n[Step 7] Model successfully saved as: {model_save_path}")

    # 10. Model Evaluation
    print("\n[Step 8] Evaluating Model Performance...")
    train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
    val_loss, val_acc = model.evaluate(X_val, y_val, verbose=0)
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

    print("\n" + "=" * 45)
    print("            MODEL EVALUATION METRICS        ")
    print("=" * 45)
    print(f"Training Loss      : {train_loss:.4f} | Training Accuracy   : {train_acc * 100:.2f}%")
    print(f"Validation Loss    : {val_loss:.4f} | Validation Accuracy : {val_acc * 100:.2f}%")
    print(f"Test Loss          : {test_loss:.4f} | Test Accuracy       : {test_acc * 100:.2f}%")
    print("=" * 45)

    # Predictions for classification report
    y_pred_probs = model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)

    print("\nClassification Report (Unseen Test Data):")
    target_names = [str(c) for c in label_encoder.classes_]
    report = classification_report(y_test, y_pred, target_names=target_names)
    print(report)

    # 11. Plot Accuracy & Loss Curves
    print("\n[Step 9] Generating Evaluation Plots...")
    epochs_range = range(1, len(history.history['accuracy']) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Accuracy Plot
    ax1.plot(epochs_range, history.history['accuracy'], 'o-', label='Training Accuracy', color='#2563eb', linewidth=2)
    ax1.plot(epochs_range, history.history['val_accuracy'], 's-', label='Validation Accuracy', color='#10b981', linewidth=2)
    ax1.set_title('Model Accuracy vs Epochs', fontsize=14, fontweight='bold', pad=12)
    ax1.set_xlabel('Epochs', fontsize=12)
    ax1.set_ylabel('Accuracy', fontsize=12)
    ax1.legend(loc='lower right', fontsize=11)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_ylim([0, 1.05])

    # Loss Plot
    ax1_loss = ax2.plot(epochs_range, history.history['loss'], 'o-', label='Training Loss', color='#ef4444', linewidth=2)
    ax2_val_loss = ax2.plot(epochs_range, history.history['val_loss'], 's-', label='Validation Loss', color='#f59e0b', linewidth=2)
    ax2.set_title('Model Loss vs Epochs', fontsize=14, fontweight='bold', pad=12)
    ax2.set_xlabel('Epochs', fontsize=12)
    ax2.set_ylabel('Sparse Categorical Crossentropy Loss', fontsize=12)
    ax2.legend(loc='upper right', fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    
    # Save plots to model directory and static images directory
    plot_path_model = os.path.join(model_dir, "evaluation_plots.png")
    plot_path_static = os.path.join(static_img_dir, "evaluation_plots.png")
    
    plt.savefig(plot_path_model, dpi=300, bbox_inches='tight')
    plt.savefig(plot_path_static, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Saved evaluation plots to:\n - {plot_path_model}\n - {plot_path_static}")
    print("\n Training Pipeline Completed Successfully!")

if __name__ == "__main__":
    train_model()
