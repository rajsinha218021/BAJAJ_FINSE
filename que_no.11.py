from datetime import datetime

# Calculate age if not already calculated
current_year = datetime.now().year
df_patient['birthDate'] = pd.to_datetime(df_patient['birthDate'], errors='coerce')
df_patient['age'] = current_year - df_patient['birthDate'].dt.year

# Extract number of medicines prescribed
df_consultation['medicine_count'] = df_consultation['medicines'].apply(len)

# Merge age and medicine count
df_combined = df_patient.merge(df_consultation, left_on='_id', right_on='_id', how='inner')

# Calculate Pearson correlation
correlation = df_combined['medicine_count'].corr(df_combined['age'])
print(round(correlation, 2)) 
# Output: -0.21
