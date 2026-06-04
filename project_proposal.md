# CFG Data Specialisation — Project Proposal

**Group Members:** Aisling, Kara, Olesya, Olivia, Raquel, and Sotiria

---

## Question 1 — Project Question

**Project Title:** Deprivation and School Performance in England (2019–2025)

**Project Question:**
How does regional deprivation affect Key Stage 4 school performance in England, and has the attainment gap between the most and least deprived Local Authorities widened or narrowed between 2019 (pre-Covid) and 2025 (post Covid)?

### Real-World Problem

Educational inequality is one of the most persistent challenges in England. Children growing up in more deprived areas consistently achieve lower grades than their peers in more affluent areas — a pattern known as the "attainment gap". Understanding where this gap is largest, which aspects of deprivation drive it most, and whether it is changing over time is essential for policymakers, schools, and charities working to level the playing field. The COVID-19 pandemic may have further widened these inequalities, making this period particularly important to study.

### Core Research Questions

1. **Performance by Deprivation Level Over Time:** How does overall school performance (Attainment 8 / Progress 8) vary between the most and least deprived Local Authorities, and has this attainment gap widened or narrowed between 2019 and 2025?

2. **Specific Deprivation Factors:** Among the different sub-domains of deprivation (Income, Employment, Health, Crime, Living Environment, Barriers to Housing), which specific factor has the strongest negative correlation with a region's educational outcomes?

3. **Subject-Specific Resilience:** Are there certain core EBacc subjects (e.g., Maths, Science) that are more resilient to the effects of deprivation compared to others (e.g., Humanities, Languages)?

4. **The Gender Gap and Deprivation:** How does the performance gap between boys and girls change across different levels of regional deprivation?

5. **Language Background and Deprivation:** How does the performance of pupils with English as an Additional Language (EAL) compare to first-language English speakers across different deprivation levels?

#### Machine Learning Questions

6. Can You Predict a School's Progress 8 Band from Non-Academic Data Alone?

7. What do "over-performing against deprivation" schools have in common — size, type, region, absence rates?

<div style="page-break-after: always;"></div>

### Scope

Our project focuses on Local Authority-level data across England, covering six academic years (2018/19 to 2024/25). The scope is realistic: we use two publicly available, well-structured datasets and our analysis is guided by the five research questions above.

### Connection to the Data Specialisation

This project draws directly on skills developed across the CFG Data Specialisation:

- **Python & Pandas** — data acquisition, cleaning, and manipulation
- **Exploratory Data Analysis (EDA)** — summary statistics, visualisations, and trend analysis
- **Statistics** — correlation analysis and comparing distributions across groups
- **Data storytelling** — communicating findings clearly to a non-technical audience

### Connection to Group Interests

Exploring real government data to surface insights about inequality in education is a motivating focus for the team.

---

## Question 2 — Target Audience

### Primary Audience

**Policymakers and local authority officers** — people who make decisions about school funding and support programmes and who need clear, evidence-based insights on where inequalities are most acute.

### Secondary Audience

**Education charities and NGOs** (e.g., Teach First, The Sutton Trust) seeking to target interventions more effectively, as well as teachers, school leaders, and researchers interested in national trends.

### Level of Expertise

Our target audience has a mixed level of data literacy. The report will be written in plain English with clear, annotated visualisations, keeping technical language to a minimum. Methodological details will be contained within the Jupyter Notebook for readers who wish to inspect them.

<div style="page-break-after: always;"></div>

## Question 3 — Data Sources

### Datasets

| Dataset | Source | Format |
|---|---|---|
| **Indices of Multiple Deprivation (IMD) 2019** — LSOA-level scores, ranks, deciles, and sub-domain indicators | Ministry of Housing, Communities & Local Government (MHCLG) via GOV.UK | CSV |
| **KS4 Pupil Characteristics and Geography** — Local Authority-level attainment by sex, language, and disadvantage status (2018/19–2024/25) | Department for Education (DfE) via the Explore Education Statistics API | CSV |

### Potential Issues and Mitigations

| Issue | Plan |
|---|---|
| **Suppressed/missing data** — The DfE dataset uses `'z'` for not applicable values and `'c'` for suppressed for small numbers | Identify and exclude suppressed values before analysis; note affected years clearly, as well as exploring factors that may contribute towards missingness (e.g. type of school, region etc.) |
| **Geographic mismatch** — IMD is at LSOA level; KS4 data is at Local Authority level | Aggregate IMD scores to Local Authority level by averaging across LSOAs within each LA |
| **COVID-19 disruption (2019/20 and 2020/21)** — No formal exams were held; results rely on teacher-assessed grades | Flag these years clearly in all charts and interpret with caution |
| **England only** — The IMD covers England only; devolved nations use different indices | Scope the analysis explicitly to England throughout |

---

## Question 4 — Team Approach

### How We Will Work Together

We plan to divide the project into workstreams broadly aligned to our research questions, with each member taking ownership of at least one area. We will also share responsibility for common tasks such as data cleaning and the final report. The specific allocation of workstreams and responsibilities will be agreed together as a team.

### Workstreams

*To be agreed by the team — broadly covering data sourcing and cleaning, one analysis area per member, and shared report writing and presentation.*
- Data sourcing, cleaning, and merging (collaborative)
- Q1 — Attainment gap over time
- Q2 — Deprivation sub-domain correlations
- Q3 — Subject-specific resilience
- Q4 — Gender gap across deprivation levels
- Q5 — EAL pupils and deprivation
- Report writing and presentation (all members)

### Team Strengths and Areas for Development

*To be discussed and completed by each team member.*
| Skill / Area | Each member to mark: Strength (S) or Area for Development (D) | Aisling | Kara | Olesya | Olivia | Raquel | Sotiria
|---|---|---|---|---|---|---|---|
| Python programming (general) | |S|D|S|D|S| |
| SQL (queries, databases, joins, aggregations) | |S|S|S|S|S| |
| Data cleaning and preprocessing with Pandas | |S|S|~|S|~| |
| Exploratory data analysis (EDA) | |S|S|S|S|S| |
| Statistical analysis (correlation, distributions) | |S|~|D|S|S| |
| Data visualisation (Matplotlib / Seaborn) | |~|~|S|~|S| |
| Working with APIs and external datasets | |S|D|D|S|~| |
| Version control with Git and GitHub | |S|S|D|S|~| |
| Report writing and data storytelling | |~|~|D|S|~| |
| Presenting findings to a non-technical audience | |D|S|D|S|S| |

### Code Management

*To be agreed by the team — likely using GitHub for version control, with a shared repository and an agreed branching strategy.*

#### Branching Strategy
- Regular git pull and/or git fetch operations 
- Branches for each research question?
- Secondary person to overview pull requests before merging to main

### Expected Project Timeline

*To be agreed by the team based on availability and submission deadline.*
| Week | Activity |
|---|---|
| Week 1 | Data sourcing and download; initial data inspection |
| | Data cleaning, handling suppressions, and merging datasets |
| Week 2 | Exploratory analysis |
| | Visualisations |
| Week 3 | Interpretation |
| | Report writing and slide preparation |
| | Peer review, final edits, and submission |
