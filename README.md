# CFG-DS-group-6-2026: Deprivation and School Performance in England (2019–2025)


## Project Overview


### Core Research Questions
1. Performance by Deprivation Level Over Time: How does overall school performance (Attainment 8 / Progress 8) vary between the most and least deprived Local Authorities, and has this attainment gap widened or narrowed between 2019 and 2025?

2. Specific Deprivation Factors: Among the different sub-domains of deprivation (Income, Employment, Health, Crime, Living Environment, Barriers to Housing), which specific factor has the strongest negative correlation with a region's educational outcomes?

3. Subject-Specific Resilience: Are there certain core EBacc subjects (e.g., Maths, Science) that are more resilient to the effects of deprivation compared to others (e.g., Humanities, Languages)?

4. The Gender Gap and Deprivation: How does the performance gap between boys and girls change across different levels of regional deprivation?

5. Language Background and Deprivation: How does the performance of pupils with English as an Additional Language (EAL) compare to first-language English speakers across different deprivation levels?

Machine Learning Questions:

6. Can You Predict a School's Progress 8 Band from Non-Academic Data Alone?

7. What do "over-performing against deprivation" schools have in common — size, type, region, absence rates?

## Data Sources

1. **DfE Key Stage 4 Performance Data**
   * **Source:** Department for Education (DfE) - Explore Education Statistics (https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/9e761bdf-fe02-4e1e-9d3d-b32dac9fa6ef)
   * **Scope:** 2009/10 to 2024/25 academic years.
   * **Key Metrics:**
   
2. **English Indices of Deprivation 2019 (IMD)**
   * **Source:** Ministry of Housing, Communities & Local Government (MHCLG) (https://www.gov.uk/csv-preview/5dc407b440f0b6379a7acc8d/File_7_-_All_IoD2019_Scores__Ranks__Deciles_and_Population_Denominators_3.csv)
   * **Scope:** Lower-layer Super Output Areas (LSOAs) aggregated to Local Authority District (LAD) level.
   * **Key Metrics:**

## Setup & Installation

### Install Dependencies
Open your terminal, navigate to this directory, and install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Jupyter Notebook
Open `.ipynb` directly inside VS Code or your preferred IDE and run it cell by cell to step through the full data science lifecycle (from data sourcing and cleaning to analysis, modeling, and conclusions).
