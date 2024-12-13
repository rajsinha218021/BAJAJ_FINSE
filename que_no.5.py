import pandas as pd

# Impute missing gender values with the mode (most frequent value)
if not df_patient['gender'].mode().empty:  # Check if mode exists to avoid errors with empty data
    mode_gender = df_patient['gender'].mode()[0]
    df_patient['gender'].fillna(mode_gender, inplace=True)

# Calculate the percentage of females ('F') in the dataset
total_count = len(df_patient)
female_count = (df_patient['gender'] == 'F').sum()

female_percentage = (female_count / total_count * 100) if total_count > 0 else 0
print(f"Percentage of Females: {round(female_percentage, 2)}%")
#output
Percentage of Females: 32.26%
