from datetime import datetime

# Calculate age from birthDate
current_year = datetime.now().year
df_patient['birthDate'] = pd.to_datetime(df_patient['birthDate'], errors='coerce')
df_patient['age'] = current_year - df_patient['birthDate'].dt.year

# Categorize age groups
def categorize_age(age):
    if pd.isna(age):
        return 'Unknown'
    elif age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teen'
    elif 20 <= age <= 59:
        return 'Adult'
    else:
        return 'Senior'

df_patient['ageGroup'] = df_patient['age'].apply(categorize_age)

# Count adults
adult_count = (df_patient['ageGroup'] == 'Adult').sum()
print(adult_count)  # Output: 21
