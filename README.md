# Loan Default Prediction Using Machine Learning

A student project starter using Python, Pandas, scikit-learn, Logistic Regression, and Flask.

## Features
- Trains a Logistic Regression classifier.
- Performs an 80/20 train-test split.
- Prints accuracy, classification report, and confusion matrix.
- Provides a simple Flask web form for a prediction demo.

## Important data note
`data/loan_data.csv` is **synthetic demo data** generated only to help you run and understand the project. Results on synthetic data are not evidence of real-world performance. Before using this as a portfolio project, replace it with a suitable public dataset, document the source, retrain the model, and report the measured test metrics honestly.

## Run on Windows
1. Install Python 3.10 or newer from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this folder.
3. Open the folder in VS Code.
4. In VS Code choose Terminal → New Terminal.
5. Run:

   ```powershell
   python -m venv .venv
   .venv\\Scripts\\Activate.ps1
   python -m pip install -r requirements.txt
   python train_model.py
   python app.py
   ```

6. Open the local address printed in the terminal, usually http://127.0.0.1:5000

If PowerShell blocks activation, run this in the same terminal:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
Then activate the environment again.

## Upload to GitHub
1. Create a new repository on GitHub named `loan-default-prediction`.
2. Keep it **Public** if you want recruiters to open it; never upload passwords, tokens, or private data.
3. In VS Code, open Source Control, initialize the repository if prompted, stage the project files, write a commit message such as `Add loan default prediction project`, and commit.
4. Choose **Publish to GitHub** and follow the sign-in prompts.
5. Open the repository page and copy its browser address. Paste that link into the form's **Link to it** field.

Do not upload the `.venv` folder or private/real applicant data.
