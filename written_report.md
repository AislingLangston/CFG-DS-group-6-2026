# Deprivation and School Performance in England (2019–2025)
## Written Report — CFG Data Science Group Project

**Group 6 Members:** Aisling, Kara, Olesya, Olivia, Raquel, and Sotiria  
**Repository:** https://github.com/AislingLangston/CFG-DS-group-6-2026  
**Date:** June 2026  

---

## 1. Introduction & Background
This project analyzes the relationship between regional deprivation—using the **2019 Indices of Multiple Deprivation (IMD)**—and **Key Stage 4 (KS4) school performance** in England.

We address the following research questions:
1. How does overall school performance vary between the most and least deprived Local Authorities, and has this attainment gap widened or narrowed between 2019 and 2025?
2. Which specific sub-domain of deprivation has the strongest negative correlation with a region's educational outcomes?
3. Are there certain core EBacc subjects (e.g., Maths, Science, Humanities, Languages) that are more resilient to the effects of deprivation compared to others?
4. How does the performance gap between boys and girls change across different deprivation levels?
5. How does the performance of pupils with English as an Additional Language (EAL) compare to first-language English speakers across different deprivation levels?
6. Can You Predict a School's Progress 8 Band from Non-Academic Data Alone?

*Target Audience:* DfE policymakers (for Pupil Premium allocation), educational charities/NGOs, and school leaders.

---

## 2. Methodology & Implementation

### Data Sourcing & Preprocessing
* **Sources:** DfE KS4 Data (2018/19–2024/25), IMD 2019 (LSOA level), and ONS boundary lookups.
* **Aggregation:** LSOA-level IMD scores were aggregated to Upper-tier Local Authority (UTLA) level using population-weighted averages.
* **Data Cleansing:** Reconciled boundary shifts (e.g., Cumbria, Northamptonshire), converted DfE suppression flags ('c', 'z') to `NaN`, and excluded COVID-affected years (2019/20 and 2020/21) due to teacher-assessment grade inflation.

### Implementation & Tools
* **Team Roles:** 
* **Stack:** Python (Pandas, NumPy, SciPy) and Matplotlib/Seaborn.

---

## 3. Results

### Q1

### Q2

### Q3

### Q4: The Gender Gap and Deprivation
* **Correlation & ANOVA:** Deprivation weakly but significantly correlates with a wider gender gap, explaining around 1.8% of the variation in that gap.
* **Impact:** The attainment gap widens with deprivation, particularly between Q4 and Q5. Compared with the least deprived group, Attainment 8 scores are 14.41% lower for boys and 12.21% lower for girls in the most deprived group, with boys experiencing a slightly greater decline overall.

<p align="center">
  <img src="pictures/gender_gap_scatter.png" width="600" alt="IMD vs Gender Gap" />
</p>

<p align="center">
  <img src="pictures/gender_gap_pct_change.png" width="350" alt="Percent Change from Q1" />
</p>

<p align="center">
  <em>Figure 3.1: Scatter plot of IMD Score vs. gender gap (top) and % change in Attainment 8 from Q1 by quintile (bottom).</em>
</p>

### Q5

### Q6

---

## 4. Conclusion & Recommendations

### Summary

### Limitations & Future Work
* **Limitations:** LA-level aggregation hides local pockets of deprivation (ecological fallacy); boundary changes limit longitudinal reliability.
* **Future Work:** Transition to school-level analysis; integrate student attendance/mental health datasets; update models when new IMD data is released.
