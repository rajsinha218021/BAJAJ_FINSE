 import pandas as pd
df_patient.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
columns_to_check = ['firstName', 'lastName', 'birthDate']
missing_percentage = (df_patient[columns_to_check].isna().mean() * 100).round(2)
print("Percentage of Missing Values:")
print(missing_percentage)
 # Output: 
 Percentage of Missing Values:
firstName    0.00
lastName    70.97
birthDate   32.26
dtype: float64

