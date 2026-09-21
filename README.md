# AI Travel Destination Recommender Using Deep Learning

An AI-based web application that recommends suitable Indian travel destinations based on user preferences such as budget, duration, season, travel type, travel preference, and region.

The system uses a trained **TensorFlow/Keras Deep Neural Network (MLP)** for destination prediction, with a **Flask backend**, user authentication, destination information, and dynamic image integration using the Unsplash API.

---

## 1. Project Overview

Planning a trip can be difficult because travelers need to consider several factors such as budget, season, location, travel duration, and type of travel.

This project provides an AI-based solution that recommends a suitable travel destination based on multiple user preferences.

The system uses a **Deep Learning Multi-Layer Perceptron (MLP)** trained with TensorFlow/Keras. The user's travel preferences are preprocessed using **OneHotEncoder** and **StandardScaler** before being passed to the neural network.

The model predicts one of **15 Indian destinations** and provides the recommended destination along with its confidence score, alternative destinations, and travel information.

---

## 2. Key Features

* **User Authentication:** Login and registration functionality with session-based authentication.
* **Deep Learning Recommendation:** Uses a trained TensorFlow/Keras neural network for destination prediction.
* **Confidence Score:** Displays the prediction probability for the recommended destination.
* **Alternative Recommendations:** Shows additional destinations based on the model's prediction probabilities.
* **Dynamic Destination Images:** Uses the Unsplash API to display destination images.
* **Travel Information:** Provides useful information such as visiting season, activities, attractions, and estimated budget.
* **Responsive Web Interface:** User-friendly travel-themed interface.
* **REST API:** Provides an `/api/recommend` endpoint for programmatic recommendations.

---

## 3. Demo Login

The application includes demo login functionality for testing.

> Demo credentials are provided within the application for testing purposes.

For security, passwords and API keys are **not stored in this public README**.

---

## 4. Technologies Used

| Category             | Technologies            |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Deep Learning        | TensorFlow, Keras       |
| Machine Learning     | Scikit-learn            |
| Data Processing      | Pandas, NumPy           |
| Model Serialization  | Joblib                  |
| Backend              | Flask, Jinja2           |
| Frontend             | HTML5, CSS3, JavaScript |
| External API         | Unsplash API            |
| Environment          | Python 3.12             |

---

## 5. System Architecture

```text
User
  ↓
Login / Registration
  ↓
Travel Preference Form
  ↓
Data Preprocessing
  ↓
OneHotEncoder + StandardScaler
  ↓
25-Dimensional Feature Vector
  ↓
TensorFlow/Keras Neural Network
  ↓
Softmax Probability Distribution
  ↓
Destination Prediction
  ↓
Confidence Score + Alternatives
  ↓
Travel Guide + Destination Image
```

---

## 6. Dataset

The project uses a dataset containing **4,500 travel records** covering **15 Indian destinations**.

### Input Features

| Feature           | Type        | Values                                                               |
| ----------------- | ----------- | -------------------------------------------------------------------- |
| Budget            | Categorical | Low, Medium, High                                                    |
| Duration          | Numerical   | 2–14 days                                                            |
| Season            | Categorical | Summer, Winter, Monsoon, Spring, Autumn                              |
| Travel Type       | Categorical | Solo, Family, Couple, Friends                                        |
| Travel Preference | Categorical | Mountains, Beach, Historical, Wildlife, Adventure, Nature, Spiritual |
| Region            | Categorical | North India, South India, East India, West India, Northeast India    |
| Destination       | Target      | 15 destination classes                                               |

### Supported Destinations

The model predicts among:

* Manali
* Goa
* Araku Valley
* Munnar
* Jaipur
* Ooty
* Mysore
* Hyderabad
* Rishikesh
* Darjeeling
* Varanasi
* Udaipur
* Andaman
* Coorg
* Kashmir

---

## 7. Data Preprocessing

The project uses the following preprocessing steps:

1. Checks the dataset for missing values.
2. Encodes destination labels using `LabelEncoder`.
3. Applies `OneHotEncoder` to categorical features.
4. Applies `StandardScaler` to the numerical duration feature.
5. Saves the preprocessing objects using Joblib.
6. Uses the same preprocessing objects during Flask-based prediction.

The processed input is converted into a **25-dimensional feature vector**.

---

## 8. Deep Learning Model

The recommendation model is a **Feedforward Deep Neural Network (MLP)** built using TensorFlow/Keras.

### Architecture

```text
Input Layer
25 Features
    ↓
Dense Layer - 128 neurons
ReLU Activation
    ↓
Batch Normalization
    ↓
Dropout - 30%
    ↓
Dense Layer - 64 neurons
ReLU Activation
    ↓
Dropout - 20%
    ↓
Dense Layer - 32 neurons
ReLU Activation
    ↓
Dense Layer - 15 neurons
Softmax Activation
    ↓
Destination Prediction
```

### Model Configuration

* **Optimizer:** Adam
* **Learning Rate:** 0.001
* **Loss Function:** Sparse Categorical Crossentropy
* **Hidden Layer Activation:** ReLU
* **Output Activation:** Softmax
* **Regularization:** Dropout and Batch Normalization

The final Softmax layer produces probabilities for the 15 destination classes.

---

## 9. Model Performance

The model was evaluated using training, validation, and unseen test data.

| Metric              | Result |
| ------------------- | -----: |
| Training Accuracy   | 94.35% |
| Validation Accuracy | 94.07% |
| Test Accuracy       | 93.78% |
| Test Loss           | 0.1180 |
| Macro F1 Score      |   0.94 |

---

## 10. Project Structure

```text
Travel-Destination-DL/
│
├── dataset/
│   └── travel_dataset.csv
│
├── model/
│   ├── train.py
│   ├── recommender.keras
│   ├── scaler.pkl
│   ├── encoders.pkl
│   └── evaluation_plots.png
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── destinations_data.py
├── generate_dataset.py
├── app.py
├── test_app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 11. Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Jayasree-2503/AI-powdered-Travel-Destination-Recommendation-Using-Deep-Learning.git
```

### Step 2: Open the Project Folder

```bash
cd AI-powdered-Travel-Destination-Recommendation-Using-Deep-Learning
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 12. Environment Variables

The project can use environment variables for external API configuration.

Create a `.env` file locally based on `.env.example`.

Example:

```text
UNSPLASH_ACCESS_KEY=your_api_key
```

### Important

Do **not** upload the `.env` file to GitHub.

Only upload:

```text
.env.example
```

Never publish private API keys, passwords, or other secret credentials.

---

## 13. Running the Project

### Run the Application

```bash
python app.py
```

The Flask application will run locally.

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

### Optional: Retrain the Model

If you want to retrain the model:

```bash
python model/train.py
```

### Run Tests

```bash
python test_app.py
```

---

## 14. How the Application Works

```text
1. User opens the application
        ↓
2. User logs in or registers
        ↓
3. User enters travel preferences
        ↓
4. Input data is preprocessed
        ↓
5. Data is passed to the trained neural network
        ↓
6. Model predicts destination probabilities
        ↓
7. Highest probability destination is selected
        ↓
8. Confidence score is calculated
        ↓
9. Alternative destinations are displayed
        ↓
10. Travel information and destination image are shown
```

---

## 15. Screenshots

Add screenshots of the application in the `screenshots/` folder.

Suggested screenshots:

```text
screenshots/
├── login.png
├── preferences.png
└── result.png
```

You can then display them in this section:

### Login Page

![Login Page](screenshots/login.png)

### Travel Preference Page

![Travel Preference Page](screenshots/preferences.png)

### Recommendation Result

![Recommendation Result](screenshots/result.png)

---

## 16. Project Demo

A demonstration video of the project is included in the repository.

The demo shows:

* User login
* Travel preference selection
* Destination prediction
* Confidence score
* Alternative recommendations
* Destination travel information
* Destination image

---

## 17. Project Documentation

The repository also contains the project documentation and presentation.

```text
docs/
├── Project_Report.pdf
└── Project_Presentation.pptx
```

---

## 18. Future Scope

The project can be extended with:

* Support for destinations outside India
* Multi-city itinerary generation
* Real-time weather information
* Real-time travel pricing
* User feedback-based model retraining
* Cloud deployment
* More personalized travel recommendations

---

## 19. Project Information

**Project Title:** AI-Powered Travel Destination Recommendation Using Deep Learning

**Domain:** Artificial Intelligence / Deep Learning

**Application:** Travel Destination Recommendation System

**Backend:** Flask

**Model:** TensorFlow/Keras MLP

**Programming Language:** Python

---

## 20. Conclusion

The project demonstrates how deep learning can be applied to travel recommendation by learning relationships between different travel preferences and destination choices.

The trained neural network provides destination recommendations based on user inputs, while the Flask web application provides an easy interface for interacting with the system.

The project combines **Deep Learning, Machine Learning preprocessing, Python, Flask, HTML, CSS, JavaScript, and API integration** to create a complete travel recommendation application.

---

## License

This project was developed as an academic/student project for educational and demonstration purposes.

Technologies used include TensorFlow/Keras, Flask, Scikit-learn, and the Unsplash API.
