import pandas as pd

# Read the Excel file
df = pd.read_excel('HR_Employee Dirty Data.xlsx', sheet_name='HRDataset_v14')

# Show basic overview
data_overview = {
    "shape": df.shape,
    "column_names": df.columns.tolist(),
    "data_types": df.dtypes,
    "missing_values": df.isnull().sum(),
    "duplicate_rows": df.duplicated().sum(),
    "preview": df.head()
 }

# Print results clearly
for key, value in data_overview.items():
 print(f"\n--- {key.upper()} ---\n{value}")

# Check how many duplicate rows exist
duplicate_count = df.duplicated().sum()
print("Duplicate rows found:", duplicate_count)

# Drop duplicates
df = df.drop_duplicates()
print("New shape after removing duplicates:", df.shape)

# Normalize text columns (strip spaces + make consistent casing)
df['Sex'] = df['Sex'].str.strip().str.title()           # e.g., "male", "M" → "Male"
df['RaceDesc'] = df['RaceDesc'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()
df['MaritalDesc'] = df['MaritalDesc'].str.strip().str.title()
df['EmploymentStatus'] = df['EmploymentStatus'].str.strip().str.title()

# Drop ID-based columns that are redundant
columns_to_drop = [
   'MarriedID', 'MaritalStatusID', 'GenderID', 'EmpStatusID',
   'DeptID', 'PerfScoreID', 'FromDiversityJobFairID', 'PositionID'
]
df.drop(columns=columns_to_drop, axis=1, inplace=True)

# Convert date columns to datetime
date_columns = ['DOB', 'DateofHire', 'DateofTermination', 'LastPerformanceReview_Date']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Show all columns with missing values
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0])

# Handle Missing Values
df['ManagerID'].fillna(0, inplace=True)
df['EngagementSurvey'].fillna(df['EngagementSurvey'].median(), inplace=True)
df['Absences'].fillna(0, inplace=True)

# Convert dates to datetime
date_columns = ['DOB', 'DateofHire', 'DateofTermination', 'LastPerformanceReview_Date']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Derived Column: IsTerminated / Attrition
df['IsTerminated'] = df['DateofTermination'].notna().astype(int)
df['AttritionFlag'] = df['DateofTermination'].notna().astype(int)

# Derived Columns: Age, Tenure
df['Age'] = (pd.Timestamp.now() - df['DOB']).dt.days // 365
df['Tenure_Years'] = ((df['DateofTermination'].fillna(pd.Timestamp.now()) - df['DateofHire']).dt.days / 365).round(1)

# Engagement Level Bucketing
def categorize_engagement(x):
    if pd.isnull(x): return 'Unknown'
    elif x < 2.5: return 'Low'
    elif x < 4: return 'Medium'
    else: return 'High'

df['EngagementLevel'] = df['EngagementSurvey'].apply(categorize_engagement)

# Handle Salary Outliers
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df.loc[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound), 'Salary'] = None

# Normalize Categorical Text
df['Sex'] = df['Sex'].str.strip().str.title()
df['RaceDesc'] = df['RaceDesc'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()
df['MaritalDesc'] = df['MaritalDesc'].str.strip().str.title()
df['EmploymentStatus'] = df['EmploymentStatus'].str.strip().str.title()

# Drop redundant columns
df.drop(columns=[
    'MarriedID', 'MaritalStatusID', 'GenderID', 'EmpStatusID',
    'DeptID', 'PerfScoreID', 'FromDiversityJobFairID', 'PositionID'
], inplace=True)

# Add Groupings
df['AgeGroup'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 100], labels=['20s', '30s', '40s', '50s', '60+'])
df['SalaryBand'] = pd.qcut(df['Salary'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

print(df.info())
print(df.head())

# Export
df.to_csv('cleaned_hr_data.csv', index=False)
print("✅ Cleaned data saved to 'cleaned_hr_data.csv'")

# 1. Load your cleaned data
df = pd.read_csv('cleaned_hr_data.csv')

# 2. Impute Salary NaNs with median (in-place)
median_salary = df['Salary'].median()
df['Salary'].fillna(median_salary, inplace=True)

# 3. Recalculate SalaryBand so it reflects the new, full Salary column
df['SalaryBand'] = pd.qcut(
    df['Salary'],
    q=4,
    labels=['Low', 'Medium', 'High', 'Very High']
)

df.loc[
  (df['ManagerName'] == 'Webster Butler') & (df['ManagerID'] == 0),
  'ManagerID'
] = 39

# 6. Save back to the same CSV (overwrites in-place)
df.to_csv('cleaned_hr_data.csv', index=False)
print("✅ cleaned_hr_data.csv updated — Salary imputed and ManagerID backfilled by Department.")

df = pd.read_csv('cleaned_hr_data.csv')

# Step 1: Convert DOB to datetime and fix future years like 2070 -> 1970
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

# Identify future DOBs incorrectly parsed as 20xx (e.g., 2070 instead of 1970)
future_dobs = df['DOB'].dt.year > 2025
df.loc[future_dobs, 'DOB'] = df.loc[future_dobs, 'DOB'] - pd.DateOffset(years=100)

# Step 2: Recalculate Age and AgeGroup
df['Age'] = (pd.Timestamp.now() - df['DOB']).dt.days // 365

df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[20, 30, 40, 50, 60, 100],
    labels=['20s', '30s', '40s', '50s', '60+']
)

# Fill missing AgeGroup with 'Unknown'
df['AgeGroup'] = df['AgeGroup'].cat.add_categories('Unknown').fillna('Unknown')

# Save updated file
df.to_csv('cleaned_hr_data.csv', index=False)

# Output a sample to verify
df[['DOB', 'Age', 'AgeGroup']].head(100)

# Reload the dataset after kernel reset
df = pd.read_csv('cleaned_hr_data.csv')

# Convert Zip to string and ensure 5-digit format
df['Zip'] = df['Zip'].astype(str).str.zfill(5)


df.to_csv('cleaned_hr_data.csv', index=False)

