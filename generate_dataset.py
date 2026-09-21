import os
import random
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# High-fidelity destination probability profiles
DESTINATIONS_CONFIG = {
    "Manali": {
        "region": ["North India"],
        "region_weights": [1.0],
        "preference": ["Mountains", "Adventure"],
        "pref_weights": [0.70, 0.30],
        "season": ["Winter", "Summer", "Spring"],
        "season_weights": [0.55, 0.35, 0.10],
        "travel_type": ["Friends", "Couple", "Solo"],
        "type_weights": [0.45, 0.40, 0.15],
        "budget": ["Medium", "High"],
        "budget_weights": [0.60, 0.40],
        "duration_range": (5, 9),
        "duration_mean": 6.5,
    },
    "Goa": {
        "region": ["West India"],
        "region_weights": [1.0],
        "preference": ["Beach", "Adventure"],
        "pref_weights": [0.80, 0.20],
        "season": ["Winter", "Monsoon", "Summer"],
        "season_weights": [0.60, 0.25, 0.15],
        "travel_type": ["Friends", "Couple", "Solo"],
        "type_weights": [0.55, 0.35, 0.10],
        "budget": ["Medium", "High", "Low"],
        "budget_weights": [0.50, 0.35, 0.15],
        "duration_range": (3, 7),
        "duration_mean": 4.8,
    },
    "Araku Valley": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Nature", "Wildlife"],
        "pref_weights": [0.75, 0.25],
        "season": ["Winter", "Monsoon", "Autumn"],
        "season_weights": [0.60, 0.25, 0.15],
        "travel_type": ["Family", "Couple"],
        "type_weights": [0.65, 0.35],
        "budget": ["Low", "Medium"],
        "budget_weights": [0.75, 0.25],
        "duration_range": (2, 4),
        "duration_mean": 2.8,
    },
    "Munnar": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Mountains", "Nature"],
        "pref_weights": [0.65, 0.35],
        "season": ["Winter", "Monsoon"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Couple", "Family"],
        "type_weights": [0.60, 0.40],
        "budget": ["Medium", "High"],
        "budget_weights": [0.65, 0.35],
        "duration_range": (3, 6),
        "duration_mean": 4.5,
    },
    "Jaipur": {
        "region": ["North India"],
        "region_weights": [1.0],
        "preference": ["Historical", "Spiritual"],
        "pref_weights": [0.75, 0.25],
        "season": ["Winter", "Spring"],
        "season_weights": [0.70, 0.30],
        "travel_type": ["Family", "Couple", "Solo"],
        "type_weights": [0.50, 0.35, 0.15],
        "budget": ["Medium", "High"],
        "budget_weights": [0.60, 0.40],
        "duration_range": (2, 5),
        "duration_mean": 3.4,
    },
    "Ooty": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Mountains", "Nature"],
        "pref_weights": [0.60, 0.40],
        "season": ["Summer", "Spring"],
        "season_weights": [0.70, 0.30],
        "travel_type": ["Family", "Couple"],
        "type_weights": [0.55, 0.45],
        "budget": ["Medium", "Low"],
        "budget_weights": [0.65, 0.35],
        "duration_range": (3, 6),
        "duration_mean": 4.0,
    },
    "Mysore": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Historical", "Spiritual"],
        "pref_weights": [0.70, 0.30],
        "season": ["Autumn", "Winter"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Family", "Solo"],
        "type_weights": [0.60, 0.40],
        "budget": ["Low", "Medium"],
        "budget_weights": [0.60, 0.40],
        "duration_range": (2, 4),
        "duration_mean": 2.6,
    },
    "Hyderabad": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Historical", "Adventure"],
        "pref_weights": [0.65, 0.35],
        "season": ["Winter", "Autumn"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Solo", "Friends"],
        "type_weights": [0.60, 0.40],
        "budget": ["Low", "Medium"],
        "budget_weights": [0.55, 0.45],
        "duration_range": (2, 4),
        "duration_mean": 2.7,
    },
    "Rishikesh": {
        "region": ["North India"],
        "region_weights": [1.0],
        "preference": ["Adventure", "Spiritual"],
        "pref_weights": [0.60, 0.40],
        "season": ["Spring", "Autumn", "Summer"],
        "season_weights": [0.45, 0.35, 0.20],
        "travel_type": ["Solo", "Friends"],
        "type_weights": [0.55, 0.45],
        "budget": ["Low", "Medium"],
        "budget_weights": [0.65, 0.35],
        "duration_range": (3, 6),
        "duration_mean": 4.0,
    },
    "Darjeeling": {
        "region": ["East India", "Northeast India"],
        "region_weights": [0.70, 0.30],
        "preference": ["Mountains", "Nature"],
        "pref_weights": [0.65, 0.35],
        "season": ["Spring", "Autumn"],
        "season_weights": [0.55, 0.45],
        "travel_type": ["Couple", "Family", "Solo"],
        "type_weights": [0.45, 0.35, 0.20],
        "budget": ["Medium", "High"],
        "budget_weights": [0.70, 0.30],
        "duration_range": (4, 7),
        "duration_mean": 5.2,
    },
    "Varanasi": {
        "region": ["North India"],
        "region_weights": [1.0],
        "preference": ["Spiritual"],
        "pref_weights": [1.0],
        "season": ["Winter", "Autumn"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Solo", "Family"],
        "type_weights": [0.55, 0.45],
        "budget": ["Low", "Medium"],
        "budget_weights": [0.75, 0.25],
        "duration_range": (2, 4),
        "duration_mean": 2.8,
    },
    "Udaipur": {
        "region": ["West India", "North India"],
        "region_weights": [0.75, 0.25],
        "preference": ["Historical", "Nature"],
        "pref_weights": [0.70, 0.30],
        "season": ["Winter", "Spring"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Couple", "Family"],
        "type_weights": [0.70, 0.30],
        "budget": ["High", "Medium"],
        "budget_weights": [0.75, 0.25],
        "duration_range": (3, 6),
        "duration_mean": 4.2,
    },
    "Andaman": {
        "region": ["South India", "East India"],
        "region_weights": [0.65, 0.35],
        "preference": ["Beach", "Adventure"],
        "pref_weights": [0.70, 0.30],
        "season": ["Winter", "Spring"],
        "season_weights": [0.65, 0.35],
        "travel_type": ["Couple", "Family", "Friends"],
        "type_weights": [0.50, 0.30, 0.20],
        "budget": ["High"],
        "budget_weights": [1.0],
        "duration_range": (6, 11),
        "duration_mean": 7.8,
    },
    "Coorg": {
        "region": ["South India"],
        "region_weights": [1.0],
        "preference": ["Nature", "Adventure"],
        "pref_weights": [0.60, 0.40],
        "season": ["Monsoon", "Winter"],
        "season_weights": [0.55, 0.45],
        "travel_type": ["Couple", "Friends"],
        "type_weights": [0.55, 0.45],
        "budget": ["Medium", "High"],
        "budget_weights": [0.65, 0.35],
        "duration_range": (2, 5),
        "duration_mean": 3.5,
    },
    "Kashmir": {
        "region": ["North India"],
        "region_weights": [1.0],
        "preference": ["Mountains", "Nature"],
        "pref_weights": [0.65, 0.35],
        "season": ["Summer", "Winter"],
        "season_weights": [0.55, 0.45],
        "travel_type": ["Couple", "Family"],
        "type_weights": [0.55, 0.45],
        "budget": ["High"],
        "budget_weights": [1.0],
        "duration_range": (6, 10),
        "duration_mean": 7.5,
    }
}

def generate_dataset(num_samples_per_dest=300):
    rows = []
    
    for dest, config in DESTINATIONS_CONFIG.items():
        for _ in range(num_samples_per_dest):
            region = np.random.choice(config["region"], p=config["region_weights"])
            pref = np.random.choice(config["preference"], p=config["pref_weights"])
            season = np.random.choice(config["season"], p=config["season_weights"])
            travel_type = np.random.choice(config["travel_type"], p=config["type_weights"])
            budget = np.random.choice(config["budget"], p=config["budget_weights"])
            
            low_dur, high_dur = config["duration_range"]
            duration = int(np.clip(round(np.random.normal(config["duration_mean"], 0.9)), low_dur, high_dur))
            
            rows.append({
                "Budget": budget,
                "Duration": duration,
                "Season": season,
                "Travel_Type": travel_type,
                "Travel_Preference": pref,
                "Region": region,
                "Destination": dest
            })
            
    df = pd.DataFrame(rows)
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    return df

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "dataset")
    os.makedirs(output_dir, exist_ok=True)
    dataset_path = os.path.join(output_dir, "travel_dataset.csv")
    
    df = generate_dataset(num_samples_per_dest=300) # Total 4,500 samples
    df.to_csv(dataset_path, index=False)
    print(f"Generated dataset with {len(df)} records across {df['Destination'].nunique()} destinations.")
    print(f"Saved to: {dataset_path}")
