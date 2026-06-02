import pandas as pd

performance_data = pd.read_csv('/Users/aislinglangston/Desktop/CFG_group_project/202425_performance_tables_schools_final.csv')

iod_data = pd.read_csv('/Users/aislinglangston/Desktop/CFG_group_project/File_7_-_All_IoD2019_Scores__Ranks__Deciles_and_Population_Denominators_3.csv')

print("---PERFORMANCE DATA STRUCTURE ------")
print(performance_data.head(10))
print(performance_data.info())

print(performance_data.columns)

print("---DEPRIVATION DATA STRUCTURE ------")
print(iod_data.head(10))
print(iod_data.info())

print(iod_data.columns)