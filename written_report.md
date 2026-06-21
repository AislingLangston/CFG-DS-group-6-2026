# Deprivation and School Performance in England (2019–2025)
## Written Report — CFG Data Science Group Project

**Group 6 Members:** Aisling Langston, Kara, Olesya, Olivia, Raquel, and Sotiria  
**Repository:** https://github.com/AislingLangston/CFG-DS-group-6-2026  
**Date:** June 2026  

---

## 1. Introduction & Background
This project analyzes the relationship between regional deprivation—using the **2019 Indices of Multiple Deprivation (IMD)**—and **Key Stage 4 (KS4) school performance** in England. GCSE outcomes are measured via **Attainment 8** (average grade across 8 subjects) and **Progress 8** (value-added). 

We address five core research questions:
1. **Performance over time:** Variations in the attainment gap between most and least deprived Local Authorities (LAs) from 2019 to 2025.
2. **Specific factors:** Which IMD sub-domains correlate strongest with poor performance.
3. **Subject resilience:** Deprivation effects on core EBacc subjects (Maths, Science) vs. Humanities/Languages.
4. **Gender gap:** How the boys/girls attainment gap changes with regional deprivation.
5. **Language background:** EAL vs. English-first performance across deprivation levels.

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
Girls consistently outperform boys in Attainment 8. Excluding COVID years, higher deprivation significantly widens this gap:
* **Correlation:** A weak but highly significant positive correlation exists between IMD score and gender gap ($r = +0.1339, p = 0.0002$).
* **ANOVA:** Gender gap differences across deprivation quintiles are statistically significant ($F = 4.4526, p = 0.00146$).
* **Post-hoc T-tests:** The gender gap in the least deprived quintile (Q1: 4.35 points) is significantly narrower than in the most deprived quintile (Q5: 4.86 points; $p = 0.00041$).
* **Insight:** Deprivation penalises boys faster than girls; from Q1 to Q3 (median deprivation), boys' scores drop by -5.63% compared to -4.33% for girls.

![IMD Score vs. Gender Gap in Attainment 8](pictures/gender_gap_scatter.png)
*Figure 3.1: Scatter plot showing positive correlation between IMD Score and gender gap (Girls - Boys Attainment 8) with fitted linear regression.*

### Q5

### Q6

---

## 4. Conclusion & Recommendations

### Summary

### Limitations & Future Work
* **Limitations:** LA-level aggregation hides local pockets of deprivation (ecological fallacy); boundary changes limit longitudinal reliability.
* **Future Work:** Transition to school-level analysis; integrate student attendance/mental health datasets; update models when new IMD data is released.
