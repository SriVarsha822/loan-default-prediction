from flask import Flask, render_template, request
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "loan_default_model.joblib"

# Train the model once before starting the Flask app.
if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Model file not found. Run: python train_model.py"
    )

model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = None

    if request.method == "POST":
        try:
            applicant_income = float(request.form["applicant_income"])
            loan_amount = float(request.form["loan_amount"])
            loan_term = float(request.form["loan_term"])
            credit_history = int(request.form["credit_history"])
            employment_years = float(request.form["employment_years"])
            existing_debt = float(request.form["existing_debt"])

            if min(applicant_income, loan_amount, loan_term,
                   employment_years, existing_debt) < 0:
                raise ValueError("Values cannot be negative.")
            if credit_history not in (0, 1):
                raise ValueError("Credit history must be 0 or 1.")

            row = pd.DataFrame([{
                "ApplicantIncome": applicant_income,
                "LoanAmount": loan_amount,
                "LoanTerm": loan_term,
                "CreditHistory": credit_history,
                "EmploymentYears": employment_years,
                "ExistingDebt": existing_debt
            }])

            result = int(model.predict(row)[0])
            prediction = (
                "Higher estimated default risk"
                if result == 1 else "Lower estimated default risk"
            )

            if hasattr(model, "predict_proba"):
                probability = float(model.predict_proba(row)[0][1]) * 100
                message = (
                    f"Demo model estimate: {probability:.1f}% default risk. "
                    "This is an educational demo, not a real lending decision."
                )
        except (ValueError, KeyError) as exc:
            message = f"Please check your inputs: {exc}"

    return render_template("index.html", prediction=prediction, message=message)

if __name__ == "__main__":
    app.run(debug=True)
