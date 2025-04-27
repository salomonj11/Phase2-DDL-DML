# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project explores machine learning approaches to predict heart disease using clinical data from multiple international datasets.  
We investigate whether prediction performance varies by **age group**, **geography**, and **clinical attribute consistency** across regions.

---

## 🧠 Research Questions

1. **Does model accuracy vary by age group?** ✅ (Answered)
2. **Are specific clinical attributes consistently predictive across geographic regions?** ✅ (Answered)
3. **Do country-specific models outperform an aggregated global model?** ✅ (Answered)

---

## 📊 Dataset Overview and Description

We combined four publicly available heart disease datasets from the UCI Heart Disease Repository:

| Dataset Source | Sample Count |
|----------------|--------------|
| Cleveland      | 297          |
| Switzerland    | 123          |
| VA             | 200          |
| Hungarian      | 294          |
| **Total**      | **914**      |

- **Target**: `num` (binary: `0 = No Heart Disease`, `1 = Heart Disease`)
- **Features (13 total)**: 
  Age, Sex, Chest Pain Type (cp), Resting Blood Pressure (trestbps), Serum Cholesterol (chol), Fasting Blood Sugar (fbs), Resting ECG (restecg), Max Heart Rate (thalach), Exercise-Induced Angina (exang), ST Depression (oldpeak), Slope, Major Vessels Colored (ca), Thalassemia Status (thal)

---

# 🔍 EDA Insights

## 🧠 Correlation Matrix

- Strongest predictors: **Chest pain type (`cp`)** and **Exercise-induced angina (`exang`)**.
- **Max heart rate (`thalach`)** and **ST depression (`oldpeak`)** also correlate meaningfully with disease.
- **Fasting blood sugar (`fbs`)** and **Resting ECG (`restecg`)** showed weak correlations.

---

## 📊 Feature Distributions

- **Age**: Heart disease cases concentrate between 55–65 years.
- **Cholesterol**: Minor distribution shifts; overlap between diseased and healthy.
- **Oldpeak**: Higher ST depression values common in heart disease.
- **Chest Pain**: Type 4 (asymptomatic) chest pain is heavily associated with heart disease.

---

# 🧩 PCA Visualization Insights

- PCA reduced the feature space to two dimensions, making decision boundaries visible.
- **PC1** mainly driven by angina, max heart rate, chest pain.
- **PC2** dominated by number of vessels, thalassemia status, and slope.
- Misclassifications occur due to information loss during 2D compression.

---

# 🌲 Random Forest Classifier Summary

- **Accuracy**: 80.33%
- **Precision**: 77.69%
- **Recall**: 91.26%
- **F1 Score**: 83.93%
- Strong recall indicates the model reliably catches true heart disease cases.

---

# ✅ Research Question #1: Does Model Accuracy Vary by Age Group?

## 💡 Logistic Regression Performance by Age Group

| Age Group | Samples | Accuracy | Precision | Recall | F1 Score |
|-----------|---------|----------|-----------|--------|----------|
| Under 45  | 194     | 0.8718    | 0.8704    | 0.8718 | 0.8636   |
| 45–60     | 499     | 0.7700    | 0.7713    | 0.7700 | 0.7699   |
| Over 60   | 221     | 0.7333    | 0.7451    | 0.7333 | 0.7378   |

---

## 🌲 Random Forest Performance by Age Group

| Age Group | Samples | Accuracy | Precision | Recall | F1 Score |
|-----------|---------|----------|-----------|--------|----------|
| Under 45  | 194     | 0.7949    | 0.7000    | 0.5833 | 0.6364   |
| 45–60     | 499     | 0.8200    | 0.8000    | 0.9123 | 0.8525   |
| Over 60   | 221     | 0.8000    | 0.8750    | 0.8485 | 0.8615   |

### 🧠 Key Insights:
- **Model performance varies by age group.**
- **Under 45**: Logistic regression performed well, Random Forest struggled more.
- **45–60**: Strongest performance across models.
- **Over 60**: Slightly lower accuracy but good precision and recall, especially for Random Forest.

---

# ✅ Research Question #2: Are Specific Clinical Attributes Consistently Predictive Across Regions?

## 🌍 Key Attribute Consistency Insights:

| Feature                        | Observations Across Datasets                                    |
|---------------------------------|------------------------------------------------------------------|
| Chest Pain Type 4               | Strongest global positive predictor everywhere                 |
| Thal: Reversible Defect         | Consistently positive across all cohorts                       |
| ST Depression (Oldpeak)         | Strong positive predictor globally                             |
| Slope of Peak ST Segment        | Consistently predictive, especially in Hungarian and Swiss data|
| Exercise-Induced Angina         | Positive predictor in most datasets                            |
| CP Type 3                       | Protective in Switzerland, less so elsewhere                   |
| Thal: Normal                    | Protective in Hungary, risky in Switzerland                    |

### 🧠 Takeaways:
- Some features (Chest Pain 4, Thal Reversible Defect, Oldpeak) are globally robust.
- Other features (like Thal Normal, Chest Pain Type 3) vary by country, suggesting clinical or measurement differences.

---

# ✅ Research Question #3: Do Country-Specific Models Outperform an Aggregated Model?

## 🌎 Country/Location vs Aggregate Model Comparison:

| Dataset      | Accuracy | Precision | Recall | F1 Score |
|--------------|----------|-----------|--------|----------|
| Cleveland    | 0.85     | 0.85      | 0.82   | 0.84     |
| Switzerland  | 0.91     | 0.91      | 0.91   | 0.91     |
| VA           | 0.78     | 0.89      | 0.80   | 0.84     |
| Hungarian    | 0.83     | 0.74      | 0.81   | 0.77     |
| **Aggregated**| **0.83** | **0.81**  | **0.89**| **0.85** |

### 🧠 Key Takeaways:

- **Switzerland-only model** achieved best performance (91% across almost all metrics).
- **Aggregated model** slightly lower accuracy than best individual model, but better generalization.
- **Country/Location-specific models** capture local patterns better, but aggregating offers better robustness for general population screening.

---

# 📁 Project Files

- `heart_disease_project.ipynb`: Main Colab Notebook
- `README.md`: This file
- `data/`: Contains the four raw UCI datasets

---

# 👥 Team

- Jesus Salomon (Team Lead)
- Nicole Mutia
- Kayla Salerno

---
