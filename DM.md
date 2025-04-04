# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project aims to develop machine learning models to predict the presence of heart disease using clinical data from multiple international datasets. We explore not just overall model performance but also how performance varies by **age group**, one of our key research questions.

---

## 🧠 Research Questions

1. **Does model accuracy vary by age group?** ✅ **(Addressed in this demo!)**
2. Are specific clinical attributes consistently predictive across geographic regions?
3. Do country-specific models outperform an aggregated global model?

---

## 📊 Dataset Summary

We merged and cleaned data from four heart disease datasets:

- **Sources**: Cleveland, Switzerland, VA, Hungarian datasets (UCI Heart Disease Repository)
- **Combined sample size**: 930 patients
- **Features**: 13 clinical attributes (e.g., age, cholesterol, chest pain type, max heart rate)
- **Target variable**: `num` — converted to binary (`0 = No Disease`, `1 = Disease`)
- **Cleaning**: Handled missing values, imputed 0 cholesterol (invalid) with column means

---

## 🔍 Exploratory Data Analysis (EDA)

- Created visualizations (e.g., histograms, KDE plots, heatmaps)
- Identified distribution patterns and correlations between features and disease status
- Noted a high number of invalid cholesterol values (mostly from Switzerland and VA datasets)

---

## 🤖 Machine Learning Models

We evaluated two baseline models:

- **Logistic Regression** (with scaling and optional PCA)
- **Random Forest Classifier**

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion matrices for model visualization

---

## ✅ Answered Research Question

### Does model accuracy vary by age group?

Yes — we trained and evaluated separate models for three age bins: **Under 45**, **45–60**, and **Over 60**.

### Logistic Regression Performance:

| Age Group | Samples | Accuracy | Precision | Recall | F1 Score |
|-----------|---------|----------|-----------|--------|----------|
| Under 45  | 194     | 0.846    | 0.833     | 0.500  | 0.625    |
| 45–60     | 499     | 0.770    | 0.741     | 0.843  | 0.789    |
| Over 60   | 221     | 0.778    | 0.800     | 0.903  | 0.848    |

#### 🔎 Observations:
- The **Under 45** group had the highest overall accuracy, but lower **recall** and **F1**, suggesting the model misses some true disease cases in younger patients.
- The **Over 60** group had the **best recall**
