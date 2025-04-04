# ❤️ Heart Disease Prediction Using Machine Learning

## 📚 Overview

This project explores machine learning models to predict the presence of heart disease in patients using clinical and demographic attributes. We expand on the original Cleveland dataset by incorporating patient data from Switzerland, VA, and Hungary — totaling **930 patient records**. Our goal is to build robust, interpretable models and analyze trends across **age groups** and **geographic regions**.

---

## 🧪 Dataset Information

We use data from the [UCI Heart Disease Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease), composed of 4 sources:

- **Cleveland (303 samples)**
- **Switzerland (123 samples)**
- **VA (49 samples)**
- **Hungary (455 samples)**

Each dataset contains **14 attributes** including:

- Demographic: `age`, `sex`
- Clinical: `cp`, `trestbps`, `chol`, `thalach`, `oldpeak`, `ca`, `thal`
- Binary/Diagnostic: `fbs`, `restecg`, `exang`, `slope`
- Target: `num` (0 = no heart disease, 1 = heart disease)

### 🛠 Data Cleaning & Preprocessing

- Missing values (`?`, `-9`) were imputed using column-wise means.
- `chol = 0` was found to be a physiologically invalid value (172 instances), especially from **Switzerland and VA**. These were replaced with the column mean.
- Final dataset: **930 clean rows**, **13 features**, and **1 target**.

---

## 🔍 Exploratory Data Analysis (EDA)

- **Correlation heatmap** revealed `cp`, `thalach`, and `oldpeak` as most predictive.
- KDEs and stacked histograms visualize key features by disease presence.
- Categorical distributions show disease is more common in males, and `cp=4` (asymptomatic chest pain) dominates heart disease cases.

EDA insights and visualizations are fully documented in the notebook.

---

## 📈 Models Built

We evaluated two models on the full dataset:

### 1. **Logistic Regression**
- Trained with scaled features and evaluated using cross-validation.
- Visualized using **PCA** to reduce features to 2D space, showing decision boundaries.
- **Metrics**:
  - Accuracy: `81.97%`
  - Precision: `80.17%`
  - Recall: `90.29%`
  - F1 Score: `84.93%`

### 2. **Random Forest Classifier**
- Added interpretability through a confusion matrix.
- Stronger performance in identifying positive cases.
- **Metrics**:
  - Accuracy: `84.15%`
  - Precision: `81.90%`
  - Recall: `92.23%`
  - F1 Score: `86.76%`

---

## 🔮 Final Stage Plan

For the final phase, we will:

- **Segment** the dataset by **age** and **region** to analyze performance across populations.
- **Answer 3 research questions**:
  1. Does model accuracy vary by age group?
  2. Are specific features consistently predictive across regions?
  3. Do region-specific models outperform global ones?
- **Optimize** hyperparameters using `GridSearchCV`.
- **Document** findings for each subgroup using visualizations and performance metrics.

---

## 👩‍🔬 Research Questions

1. **Age Accuracy**: Does model performance differ by patient age group?
2. **Predictive Consistency**: Are certain features consistently strong predictors regardless of dataset origin?
3. **Regional Specialization**: Do models trained on one country outperform generalized models for that population?

---

## 📁 Repository Structure

```
├── data/
│   ├── processed.cleveland.data
│   ├── processed.switzerland.data
│   ├── processed.va.data
│   └── reprocessed.hungarian.data
├── Heart_Disease_Prediction_Final_Demo.ipynb
└── README.md
```

---

## 🙌 Team Members

- Jesus Salomon (Team Lead)
- Nicole Mutia
- Kayla Salerno
