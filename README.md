# 💰 Loan Default Prediction Using Machine Learning

## 📌 Overview

This project is a Machine Learning web application that estimates loan default risk based on applicant details. It uses a Logistic Regression model and a Flask-based web interface to display risk predictions.

The application considers factors such as monthly income, loan amount, loan term, credit history, years employed, and existing monthly debt.

---

## 🚀 Features

- 📊 Loan Default Risk Prediction
- 💰 Applicant Income and Loan Amount Analysis
- 🏦 Credit History Evaluation
- 💼 Employment and Existing Debt Consideration
- 🤖 Machine Learning-Based Prediction
- 🌐 User-Friendly Flask Web Interface
- 📱 Simple and Responsive Design

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3
- Git & GitHub

---

## 🤖 Machine Learning Algorithm

**Logistic Regression**

Logistic Regression is a supervised machine learning algorithm used for classification. In this project, it estimates the likelihood of loan default based on the applicant's input details.

**Dataset:** Synthetic demo data generated for educational purposes.

**Important:** Results from synthetic data do not demonstrate real-world model performance. The model must be evaluated using a suitable public dataset before practical use.

---

## 📂 Project Structure

```text
loan-default-prediction/
│
├── app.py
├── train_model.py
├── loan_default_model.joblib
├── requirements.txt
├── README.md
│
├── data/
│   └── loan_data.csv
│
└── templates/
    └── index.html
```

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/SriVarsha822/loan-default-prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd loan-default-prediction
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

```bash
python train_model.py
```

### 5. Run the Flask Application

```bash
python app.py
```

### 6. Open in Browser

Open the local address displayed in the terminal, usually:

http://127.0.0.1:5000

---

## ⚠️ Important Disclaimer

This project is an educational demonstration using synthetic data. It is not a validated credit-scoring system and should not be used to make actual lending or financial decisions.

---

## 👩‍💻 Author

**Varsha Chakravarthula**

B.Tech — Artificial Intelligence and Machine Learning
