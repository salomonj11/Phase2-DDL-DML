# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project explores machine learning approaches to predict heart disease using clinical data from multiple international datasets. It also investigates whether prediction performance varies by age group, geography, and clinical attribute consistency.

---

## 🧠 Research Questions

1. **Does model accuracy vary by age group?** ✅ **(Answered in this demo)**
2. Are specific clinical attributes consistently predictive across geographic regions?
3. Do country-specific models outperform an aggregated global model?

---

## 📊 Dataset Overview and Description

We combined four publicly available heart disease datasets from the UCI Heart Disease Repository:

| Dataset Source | Sample Count |
|----------------|---------------|
| Cleveland      | 297           |
| Switzerland    | 123           |
| VA             | 200            |
| Hungarian      | 294           |
| **Total**      | **914**       |

- **Target**: `num` (reclassified to binary: `0 = No Heart Disease`, `1 = Heart Disease`)
- **Features (13 total)**:
  - `age`: Patient age in years
  - `sex`: 1 = male; 0 = female
  - `cp`: Chest pain type (4 categories)
  - `trestbps`: Resting blood pressure (mm Hg)
  - `chol`: Serum cholesterol (mg/dl) → *Imputed 172 values where cholesterol was 0*
  - `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
  - `restecg`: Resting ECG results (0–2)
  - `thalach`: Max heart rate achieved
  - `exang`: Exercise-induced angina (1 = yes; 0 = no)
  - `oldpeak`: ST depression induced by exercise
  - `slope`: Slope of ST segment (0–2)
  - `ca`: Number of major vessels colored by fluoroscopy (0–3)
  - `thal`: 3 = normal, 6 = fixed defect, 7 = reversible defect

---

## 📈 Distribution Insights

We conducted Exploratory Data Analysis (EDA) to uncover key patterns:

- **Age**: Most patients with heart disease are aged 55–65; younger patients are less represented.
- **Cholesterol (`chol`)**:
  - Notably, 172 records had invalid `chol = 0`, mostly from Switzerland and VA datasets.
  - After imputing, we observed overlapping distributions between those with and without heart disease.
- **Chest Pain Type (`cp`)**:
  - Type 4 (asymptomatic) is heavily associated with heart disease.
- **Max Heart Rate (`thalach`)**:
  - Lower values more commonly occur in patients with heart disease.
- **Exercise Angina (`exang`)**:
  - Strongly associated with heart disease presence.
- **Sex**:
  - Males are overrepresented in the dataset and have higher disease rates.

---

## 🤖 Models Implemented

We trained and evaluated the following baseline models:

- **Logistic Regression**
- **Random Forest Classifier**

Evaluation metrics for all models include:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix Visualization

---

## ✅ Research Question Answered

### 🔍 Does model accuracy vary by age group?

Yes — we segmented patients into three age groups and trained separate models per group.

| Age Group | Samples | Accuracy | Precision | Recall | F1 Score |
|-----------|---------|----------|-----------|--------|----------|
| Under 45  | 194     | 0.846    | 0.833     | 0.500  | 0.625    |
| 45–60     | 499     | 0.770    | 0.741     | 0.843  | 0.789    |
| Over 60   | 221     | 0.778    | 0.800     | 0.903  | 0.848    |

### 🧠 Insights:

- Model **recall is low for patients under 45**, possibly due to lower prevalence or subtler signs of disease.
- The **Over 60** group had the best balance of recall and F1 score, making it the most effective segment for disease identification.
- These results support the idea that **age-aware modeling or stratified approaches** could improve predictive reliability across populations.

---

## 📁 Project Files

- `heart_disease_project.ipynb`: Main Colab Notebook with full pipeline (upload, clean, visualize, model, evaluate)
- `README.md`: This file
- `data/`: Contains the four raw UCI datasets

---

## 🔜 Next Steps

- Answer remaining research questions:
  - Attribute consistency across regions
  - Country-specific vs global models
- Hyperparameter tuning (e.g., Random Forest depth, Logistic regularization)
- Add neural networks and ensemble comparisons
- Use SHAP/feature importance to improve interpretability

---

## 👥 Team

- Jesus Salomon (Team Lead)
- Nicole Mutia
- Kayla Salerno

---
