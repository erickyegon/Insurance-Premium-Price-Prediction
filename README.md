# Insurance Premium Prediction Project

## Problem Statement

Shield Insurance Company faced challenges in accurately predicting insurance premiums for its customers, particularly for younger age groups (25 and under). The existing model had significant error rates, leading to customer dissatisfaction and operational inefficiencies.

### Key Issues:
- The overall model accuracy was **92%**, but certain customer segments experienced high error rates.
- **30% of predictions** had error margins greater than 10%.
- Some predictions had error margins as high as **87%**.
- The model performed poorly for customers aged **25 and under**, requiring a more tailored solution for this group.

## Our Approach

To tackle these challenges, we implemented a structured approach that balanced technical rigor and business needs. This approach included:

1. **Data Analysis and Preprocessing**
2. **Feature Engineering**
3. **Model Development**
4. **Model Segmentation**
5. **Error Analysis**
6. **Iterative Improvement**

### 1. Data Analysis and Preprocessing
- **Data Cleaning**: Removed missing values, handled outliers, and standardized the dataset.
- **Exploratory Data Analysis (EDA)**: Investigated feature distributions and relationships to understand which factors influence premiums.
- **Normalization and Scaling**: Applied transformations to ensure consistent feature scales, which helps models perform better.

### 2. Feature Engineering
- **Risk Score**: Developed a **normalized risk score** based on medical history to quantify a customer’s health risks.
- **Encoding**: Used **one-hot encoding** for non-ordered categorical variables (e.g., gender, region) and **label encoding** for ordered categories (e.g., insurance plan tiers like Bronze, Silver, Gold).

### 3. Model Development
We tested several machine learning models to find the best approach:
- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **XGBoost**

**XGBoost** outperformed the others, particularly for customers aged **over 25**, providing superior accuracy and error control.

### 4. Model Segmentation
Given the model's poor performance for younger customers, we segmented the model into two distinct groups:
- **Model A**: Targeted customers aged **25 and under**.
- **Model B**: Handled customers aged **over 25**.

This allowed us to tailor feature engineering and model optimization to each group’s specific characteristics.

### 5. Error Analysis
To improve accuracy:
- We visualized and analyzed error patterns using **histograms** and **distribution plots**.
- These insights helped identify which features caused the most errors, particularly for younger customers, and guided model refinements.

### 6. Iterative Improvement
By continuously analyzing errors and refining the models:
- We introduced new features (e.g., lifestyle factors, genetic risk, and past claims) to enhance predictions.
- Collaborated with business stakeholders to ensure the model aligned with real-world business needs.

---

## Key Decisions and Rationale

- **Model Segmentation**: We divided the model by age group because younger customers’ premium predictions were significantly less accurate. By developing separate models for customers above and below 25, we tailored our approach to improve accuracy.
  
- **XGBoost for Model B**: For customers over 25, **XGBoost** delivered excellent results, achieving **99% accuracy** and minimizing prediction errors.

- **Linear Regression for Model A**: While **linear regression** for younger customers provided a baseline accuracy of **60%**, it highlighted areas for further improvement. This model allowed for better interpretability, providing a starting point for future refinement.

- **Risk Score**: The risk score created from medical history became one of the most important features in predicting premiums. This feature contributed significantly to model performance improvements.

- **Error Analysis**: Rigorous error analysis, including tracking errors by age group and feature, was crucial in identifying opportunities for refining the models.

---

## Findings and Results

### Model B (Customers Over 25):
- **99% accuracy** using XGBoost.
- Only **0.3%** of predictions had an error margin greater than 10%, a major improvement over the initial model.
- This model showed significantly improved performance compared to the original, meeting the accuracy requirement for Shield Insurance's business needs.

### Model A (Customers 25 and Under):
- Initial accuracy of **60%** using linear regression.
- The model highlighted areas needing improvement, particularly through additional features like lifestyle factors and genetic risk.
- Further feature engineering and data collection are necessary to bring the model’s performance to acceptable levels.

### Overall Insights:
- **Age** is a key determinant in predicting insurance premiums, and different age groups require different models for optimal performance.
- **Medical history** is an important predictor of insurance premiums, especially when encoded as a risk score.
- **Segmentation** of models based on age was critical in achieving high accuracy for older customers while identifying paths to improvement for younger customers.

---

## Requirements and How They Were Achieved

### Requirements:
1. **Accurate Premium Prediction**: Achieve high model accuracy (>97%) to ensure precise premium calculations.
2. **Error Control**: Ensure that at least 95% of predictions have an error margin of less than 10%.
3. **Cloud Deployment**: Make the model accessible to underwriters via a cloud-based solution.
4. **Segmented Models**: Address the performance issues for younger customers (25 and under) with a tailored solution.

### Achievements:
- **High Accuracy**: **Model B** for customers over 25 achieved **99% accuracy** using XGBoost, surpassing the 97% target. This met the requirement for precise premium prediction.
- **Error Control**: With **0.3%** of predictions exceeding the 10% error margin for Model B, we far exceeded the 95% goal.
- **Streamlit Deployment**: We deployed the model on **Streamlit**, providing a web-based application accessible to insurance underwriters. They can now input customer data and receive real-time premium predictions from any location.
- **Model Segmentation**: By creating **Model A** and **Model B**, we addressed the unique challenges posed by different age groups, improving accuracy for older customers and setting a baseline for younger customers.

---

## Next Steps

- **Data Collection**: Gather additional data on lifestyle factors, genetic risk, and past insurance claims to improve the accuracy of **Model A** (younger customers).
- **Model Refinement**: Continue refining **Model A** by experimenting with additional features and improving the accuracy for customers aged 25 and under.
- **Production Pipeline**: Implement a full production pipeline that automatically routes predictions through the appropriate model (Model A or B) based on the customer’s age, ensuring optimal predictions.
- **Scaling**: Optimize the **Streamlit** deployment for larger datasets and more concurrent users, ensuring smooth performance as usage scales.

---

By meeting the project’s requirements through thoughtful segmentation, ongoing model improvement, and cloud deployment, we’ve significantly enhanced Shield Insurance’s ability to predict insurance premiums. While we have achieved optimal performance for customers over 25, there remains ongoing work to improve predictions for younger customers, ensuring the same level of accuracy across all segments.
