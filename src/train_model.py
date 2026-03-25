import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load data
df = pd.read_csv("data/student_data.csv")

# Features & target
X = df.drop("final_score", axis=1)
y = df["final_score"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ FIXED MODEL (stable + supports feature importance)
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("models/model.pkl", "wb"))

print("✅ Model trained and saved successfully!")