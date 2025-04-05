# 💰 Waiter Tip Prediction using Machine Learning (Regression)
<img src="https://github.com/goldstring/waiter_tip_prediction_using_machine_learning_regression_end_to_end_project/blob/main/22676373_80_d2luZXJ5LTA3.jpg?raw=true" />

This project uses machine learning regression techniques to predict the amount of tip a customer might give based on features such as total bill, gender, smoking status, time of day, and day of the week. A user-friendly web application is created using Streamlit for interactive tip predictions.

---

## 🧠 Problem Statement

In the hospitality industry, predicting waiter tips can help restaurants analyze customer behavior, optimize service strategies, and ensure fair staff compensation. This project aims to build a regression model that predicts the tip amount based on various input features like bill amount, customer demographics, and time.

---

## 🏠 Industry

Hospitality, Food & Beverage

---

## 🌐 Domain

Customer Behavior Analytics, Predictive Analytics, Restaurant Operations

---

## 📊 Dataset Explanation

The dataset used is the **Tips Dataset** from the Seaborn library, which contains information about:

- `total_bill` – total bill amount (float)
- `tip` – tip amount (target variable) (float)
- `sex` – gender of the customer (Male/Female)
- `smoker` – whether the customer is a smoker (Yes/No)
- `day` – day of the week (Thur, Fri, Sat, Sun)
- `time` – Lunch or Dinner
- `size` – number of people in the group

The dataset has 244 entries and is ideal for linear regression and exploratory data analysis.

---

## 🤖 Model Used

- **Linear Regression**
  - Achieved **R² score = 0.934** on test data.
  - Trained using scikit-learn with data preprocessing (label encoding and scaling).

---

## 📈 Model Performance

### R² Score:

```
Linear Regression R²: 0.934
```

### 📸 Screenshot:

<img src="https://github.com/goldstring/waiter_tip_prediction_using_machine_learning_regression_end_to_end_project/blob/main/output/model_performance.png?raw=true" />

---

## 🚀 Installation and Running the Application

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/waiter-tip-prediction.git
cd waiter-tip-prediction
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On Mac/Linux:

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit app

```bash
streamlit run app.py
```

---


## 🧾 Output Example
<img src="https://github.com/goldstring/waiter_tip_prediction_using_machine_learning_regression_end_to_end_project/blob/main/output/screenshots.png?raw=true" />


## ✅ Conclusion

This project demonstrates how regression models can be used to predict waiter tips with high accuracy. Using a simple yet powerful model like Linear Regression, the app provides real-time predictions and can serve as a foundational tool for tipping behavior analysis in restaurants.

---


## 📬 Contact

For queries, suggestions, or collaborations, feel free to reach out!
