import numpy as np
import pandas as pd

'''
# COLUMNS TO RETAIN IN PERFORMANCE TABLE
Identifiers and filters
- new_la_code/la_name - for joining to deprivation dataset
- school_urn/school_name - unique school id
- establishment_type_group - academy, independent, maintained
- sex
- disadvantage_status
- first_language
- breakdown_topic


Outcome measures
- attainment8_average
- progress8_average
- progress8_lower_95_ci / progress8_upper_95_ci
- ebacc_aps_average

Subject-specific (for Q3)
- attainment8eng_average, attainment8mat_average, attainment8ebacc_average
- progress8eng_average, progress8mat_average, progress8ebacc_average, progress8open_average
- ebacceng_95_percent, ebaccmat_95_percent, ebaccsci_95_percent, ebacchum_95_percent, ebacclan_95_percent

Pupil characteristics
- pupil_count


# COLUMNS TO RETAIN IN DEPRIVATION DATA
Identifier
- Local Authority District code (2019)

Deprivation (for Q1)
- Index of Multiple Deprivation (IMD) Score

Specific Deprivation Factors (for Q2)
- Income Score (rate)
- Employment Score (rate)
- Health Deprivation and Disability Score
- Crime Score
- Barriers to Housing and Services Score
- Living Environment Score
- Income Deprivation Affecting Children Index (IDACI) Score (rate)
- Children and Young People Sub-domain Score

'''


performance_data = pd.read_csv('/Users/aislinglangston/Desktop/CFG_group_project/202425_performance_tables_schools_final.csv')

iod_data = pd.read_csv('/Users/aislinglangston/Desktop/CFG_group_project/File_7_-_All_IoD2019_Scores__Ranks__Deciles_and_Population_Denominators_3.csv')

# Filtering performance rows (several per school, so trimming down) & columns
performance_total = performance_data[
    (performance_data['breakdown_topic'] == 'Total') &
    (performance_data['sex'] == 'Total') &
    (performance_data['disadvantage_status'] == 'Total') &
    (performance_data['first_language'] == 'Total')
][['school_urn', 'school_name', 'la_name', 'new_la_code',
   'establishment_type_group', 'pupil_count',
   'attainment8_average', 'progress8_average', 
   'ebacc_aps_average']].copy()



# For Q4 (gender gap) - use sex breakdown
perf_gender = performance_data[
    (performance_data['breakdown_topic'] == 'Sex') &
    (performance_data['disadvantage_status'] == 'Total') &
    (performance_data['first_language'] == 'Total')
][['school_urn', 'school_name', 'la_name', 'new_la_code',
   'establishment_type_group', 'pupil_count',
   'attainment8_average', 'progress8_average', 
   'ebacc_aps_average']].copy()

# For Q5 (EAL) - use first language breakdown
perf_eal = performance_data[
    (performance_data['breakdown_topic'] == 'First language')
][['school_urn', 'school_name', 'la_name', 'new_la_code',
   'establishment_type_group', 'pupil_count',
   'attainment8_average', 'progress8_average', 
   'ebacc_aps_average']].copy()

print("---NEW PERFORMANCE DATA STRUCTURE ------")
print(performance_total.head(10))
print(performance_total.info())
print(performance_total.columns)


iod_la = iod_data.groupby(
    ['Local Authority District code (2019)', 'Local Authority District name (2019)']
).agg(
    imd_score          = ('Index of Multiple Deprivation (IMD) Score', 'mean'),
    income_score       = ('Income Score (rate)', 'mean'),
    employment_score   = ('Employment Score (rate)', 'mean'),
    health_score       = ('Health Deprivation and Disability Score', 'mean'),
    crime_score        = ('Crime Score', 'mean'),
    barriers_score     = ('Barriers to Housing and Services Score', 'mean'),
    living_env_score   = ('Living Environment Score', 'mean'),
    idaci_score        = ('Income Deprivation Affecting Children Index (IDACI) Score (rate)', 'mean'),
    children_subdomain = ('Children and Young People Sub-domain Score', 'mean'),
).reset_index()

iod_la.rename(columns={
    'Local Authority District code (2019)': 'la_code'
}, inplace=True)

print("---NEW DEPRIVATION DATA STRUCTURE ------")
print(iod_la.head(10))
print(iod_la.info())


# MISSING DATA
print("--- MISSING DATA INITIAL ANALYSIS---")
# Per column counts
c_by_col = (performance_total == 'c').sum()
z_by_col = (performance_total == 'z').sum()

# Show only columns that actually have them
performance_total_suppression_summary = pd.DataFrame({
    'c_count': c_by_col,
    'z_count': z_by_col
})
performance_total_suppression_summary = performance_total_suppression_summary[
    (performance_total_suppression_summary['c_count'] > 0) | 
    (performance_total_suppression_summary['z_count'] > 0)
].sort_values('c_count', ascending=False)

print(f"Performance total supression summary: \n {performance_total_suppression_summary}")


# Gender 
# Per column counts
c_by_col = (perf_gender == 'c').sum()
z_by_col = (perf_gender == 'z').sum()

# Show only columns that actually have them
perf_gender_suppression_summary = pd.DataFrame({
    'c_count': c_by_col,
    'z_count': z_by_col
})
perf_gender_suppression_summary = perf_gender_suppression_summary[
    (perf_gender_suppression_summary['c_count'] > 0) | 
    (perf_gender_suppression_summary['z_count'] > 0)
].sort_values('c_count', ascending=False)

print(f"Performance gender supression summary: \n {perf_gender_suppression_summary}")

# EAL
# Per column counts
c_by_col = (perf_eal == 'c').sum()
z_by_col = (perf_eal == 'z').sum()

# Show only columns that actually have them
perf_eal_suppression_summary = pd.DataFrame({
    'c_count': c_by_col,
    'z_count': z_by_col
})
perf_eal_suppression_summary = perf_eal_suppression_summary[
    (perf_eal_suppression_summary['c_count'] > 0) | 
    (perf_eal_suppression_summary['z_count'] > 0)
].sort_values('c_count', ascending=False)

print(f"Performance EAL supression summary: \n {perf_eal_suppression_summary}")
