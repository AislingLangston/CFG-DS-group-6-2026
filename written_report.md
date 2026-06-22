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
6. Which Local Authorities consistently outperform or underperform their predicted Attainment 8 score, and is there a geographic pattern among these outliers?

*Target Audience:* DfE policymakers (for Pupil Premium allocation), educational charities/NGOs, and school leaders.

---

## 2. Methodology & Implementation

### Data Sourcing & Preprocessing
* **Sources:** DfE KS4 Data (2018/19–2024/25), IMD 2019 (LSOA level), and ONS boundary lookups.
* **Aggregation:** LSOA-level IMD scores were aggregated to Upper-tier Local Authority (UTLA) level using population-weighted averages.
* **Data Cleansing:** Reconciled boundary shifts (e.g., Cumbria, Northamptonshire), converted DfE suppression flags ('c', 'z') to `NaN`, and excluded COVID-affected years (2019/20 and 2020/21) due to teacher-assessment grade inflation.


#### Question 6 Methodology

To identify Local Authorities that perform differently from what would be expected from their deprivation level, a linear regression model was fitted between IMD score and Attainment 8 average for each examined year separately. The residual, that is, the difference between each LA's actual and predicted Attainment 8 score, was used as the measure of over- or underperformance. A positive residual indicates an LA achieving better than its deprivation level predicts, while a negative residual indicates underperformance.

Mean residuals were calculated for each LA across all five examined years to identify consistent rather than incidental over- or underperformance. LAs whose mean residual fell more than one standard deviation above or below the mean were classified as Overperformers or Underperformers respectively.

Given the identification of over-perfomers as dominated by London LAs, Local Authorities were classified as London or non-London using ONS borough boundaries. Separate linear regression lines were fitted for each group to compare the deprivation-attainment relationship between them. Year-by-year residuals were examined for all flagged LAs to assess consistency of over- and underperformance across the five examined years, and a trend measure was calculated by comparing each LA's 2024/25 residual against its 2018/19 residual. Deprivation sub-domain profiles were compared across performance groups using mean scores and box plots, and stratified by London membership to test whether any sub-domain effect was independent of geography.

### Implementation & Tools
* **Team Roles:** 
After the initial data cleaning, each member of the team took the lead on a separate RQ.
Question 1: Soteria
Question 2: Olivia
Question 3: Olesya
Question 4: Raquel
Question 5: Kara
Question 6: Aisling 


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

Nineteen LAs were classified as consistent overperformers and twenty as consistent underperformers across the five examined years. In Table 6.1, the top five overperfomers are listed, together with their mean residual, and identification as London or non-London borough. In Table 6.2, the underperformers are similarly reported. London LAs are over-represented in the top performers, while they are under-represented in underperformers.

Of the 19 outperforming LAs (full list is avaiable in the jupyter notebook), 14 are London boroughs. No London borough appears in the underperformer group. This is consistent with the well-documented "London Effect" — a pattern of sustained educational outperformance relative to deprivation documented in DfE research (see for example, Ross et al., 2020).

The regression plot (Figure 6.1) illustrates this clearly. London boroughs, as shown in red achieve higher Attainment 8 scores than non-London LAs (in blue) at every comparable deprivation level. However, it is interesting to note that the slope is steeper for London LAs than for non-London LAs, suggesting that London's attainment advantage over non-London LAs at comparable deprivation levels is largest among less deprived boroughs and narrows as deprivation increases. Therefore, the London Effect is not uniform across the deprivation spectrum. However, the London LAs have a lower limit to their IMD score than non-London LAs (London IMD scores range from approximately 9 to 33, while the most deprived non-London LA), which means that this 

It is also worth observing the residual distribution. The positive tail is notably longer than the negative tail (maximum +10.09, minimum -6.65), suggesting that the factors enabling some LAs to exceed deprivation predictions are more powerful in magnitude than the factors causing others to fall short. Further research in this area may be warranted.

<p align="center">
  <em>Table 6.1: Outperformers (Top 5 by Mean Residual)</em>
</p>

<p align="center">
| Rank | Local Authority | Mean Residual | London Borough |
|---|---|---|---|
| 1 | Sutton | +10.09 | Yes |
| 2 | Trafford | +8.61 | No |
| 3 | Kingston upon Thames | +8.54 | Yes |
| 4 | Hammersmith and Fulham | +8.47 | Yes |
| 5 | Barnet | +8.41 | Yes |
</p>



<p align="center">
  <em>Table 6.2: Underperformers (Bottom 5 by Mean Residual)</em>
</p>

<p align="center">
| Rank | Local Authority | Mean Residual |
|---|---|---|
| 1 | Knowsley | -6.65 |
| 2 | Central Bedfordshire | -5.73 |
| 3 | Portsmouth | -5.36 |
| 4 | South Gloucestershire | -5.30 |
| 5 | Isle of Wight | -4.85 |
<p>

<p align="center">
  <img src="pictures/london_vs_non-london_dep_vs_attainment.png" width="350" alt="Percent Change from Q1" />
</p>

<p align="center">
  <em>Figure 6.1: Scatter plot of IMD Score vs. residuals for Attainment 8, separated into London and non-London LAs.</em>
</p>

---

## 4. Conclusion & Recommendations

### Summary

### Limitations & Future Work
* **Limitations:** LA-level aggregation hides local pockets of deprivation (ecological fallacy); boundary changes limit longitudinal reliability.
* **Future Work:** Transition to school-level analysis; integrate student attendance/mental health datasets; update models when new IMD data is released. Future studies into the efficacy of non-academic interventions to increase attainment would therefore merit investigation into the structural, cultural and other areas of difference between London and the rest of England.


## Bibliography

- Ross, A., Lessof, C., Brind, R., Khandker, R. and Aitken, D. (2020) Examining the London advantage in attainment: evidence from LSYPE. London: Department for Education. Available at: https://assets.publishing.service.gov.uk/media/5fb7cc538fa8f559dbb1ad4b/London_effect_report_-_final_20112020.pdf (Accessed: 19 June 2026).