import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = pd.DataFrame({
    "study_hours": np.random.uniform(1, 10, n),
    "attendance": np.random.uniform(50, 100, n),
    "previous_score": np.random.uniform(40, 100, n),
    "sleep_hours": np.random.uniform(4, 9, n),
    "internet_usage": np.random.uniform(1, 8, n),
    "extracurricular": np.random.choice([0, 1], n),
    "parent_education": np.random.choice([1, 2, 3], n)
})

data["final_score"] = (
    data["study_hours"] * 5 +
    data["attendance"] * 0.3 +
    data["previous_score"] * 0.4 +
    data["sleep_hours"] * 2 -
    data["internet_usage"] * 1.5 +
    data["extracurricular"] * 2 +
    data["parent_education"] * 3 +
    np.random.normal(0, 5, n)
)

data["final_score"] = data["final_score"].clip(0, 100)

data.to_csv("data/student_data.csv", index=False)

print("Dataset created successfully!")