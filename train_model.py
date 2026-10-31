from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "loan_data.csv"
MODEL_PATH = BASE_DIR / "loan_default_model.joblib"

FEATURES = [
    "ApplicantIncome", "LoanAmount", "LoanTerm",
    "CreditHistory", "EmploymentYears", "ExistingDebt"
]
TARGET = "Default"

def main():
    data = pd.read_csv(DATA_PATH)
    missing = [c for c in FEATURES + [TARGET] if c not in data.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    X = data[FEATURES]
    y = data[TARGET].astype(int)

    numeric_features = [
        "ApplicantIncome", "LoanAmount", "LoanTerm",
        "EmploymentYears", "ExistingDebt"
    ]
    binary_features = ["CreditHistory"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    binary_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent"))
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("binary", binary_pipeline, binary_features)
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Test accuracy: {accuracy_score(y_test, predictions):.3f}")
    print("\nClassification report:\n", classification_report(y_test, predictions))
    print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
    print("\nIMPORTANT: data/loan_data.csv contains synthetic demo data.")
    print("Do not report this score as real-world performance.")
    joblib.dump(model, MODEL_PATH)
    print(f"\nSaved model to: {MODEL_PATH}")

if __name__ == "__main__":
    main()
