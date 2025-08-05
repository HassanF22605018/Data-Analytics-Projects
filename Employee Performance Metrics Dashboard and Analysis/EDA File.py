# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_hr_data.csv")

# 1. Dataset Overview
print("Dataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# 2. Descriptive Statistics for numeric columns
numeric_cols = ['Salary', 'Age', 'Tenure_Years', 'EngagementSurvey', 'EmpSatisfaction', 'Absences']
print("\nDescriptive Statistics:\n", df[numeric_cols].describe())

# 3. Categorical Feature Analysis
cat_cols = [
    'Department', 'EmploymentStatus', 'MaritalDesc', 'Sex', 'RaceDesc',
    'RecruitmentSource', 'PerformanceScore', 'EngagementLevel', 'SalaryBand',
    'AgeGroup', 'AttritionFlag', 'IsTerminated'
]

for col in cat_cols:
    print(f"\nValue counts for {col}:\n{df[col].value_counts(normalize=True) * 100}")
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"{col} Distribution")
    plt.tight_layout()
    plt.show()

# 4. Attrition and Termination Analysis
terminated = df[df['IsTerminated'] == True]
active = df[df['IsTerminated'] == False]

# Attrition by Department, AgeGroup, Gender, PerformanceScore
group_cols = ['Department', 'AgeGroup', 'Sex', 'PerformanceScore']
for col in group_cols:
    ctab = pd.crosstab(df[col], df['AttritionFlag'], normalize='index') * 100
    ctab.plot(kind='bar', stacked=True, title=f'Attrition by {col}', figsize=(8, 4))
    plt.ylabel("Percentage")
    plt.legend(title="AttritionFlag")
    plt.tight_layout()
    plt.show()

# Correlation between Absences, Tenure, Attrition
df['AttritionFlagNum'] = df['AttritionFlag'].astype(int)
print("\nCorrelation between Absences, Tenure, and Attrition:\n")
print(df[['Absences', 'Tenure_Years', 'AttritionFlagNum']].corr())

# 5. Absence Analysis
plt.figure(figsize=(6, 4))
sns.histplot(df['Absences'], bins=20, kde=True)
plt.title("Absences Distribution")
plt.show()

# High Absentees
high_abs = df[df['Absences'] > 15]
print("\nHigh Absentees (>15 days):", len(high_abs))
print(high_abs[['Employee_Name', 'Absences']])

# Absences vs EngagementSurvey
sns.scatterplot(data=df, x='Absences', y='EngagementSurvey')
plt.title("Absences vs EngagementSurvey")
plt.show()

# Absences vs EmpSatisfaction
sns.scatterplot(data=df, x='Absences', y='EmpSatisfaction')
plt.title("Absences vs EmpSatisfaction")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 7. Extra Patterns / Hypotheses
# You can try: df.groupby('Department')['Salary'].mean().sort_values(ascending=False)

print("\nYou can now formulate business hypotheses such as:\n")
print("- Does low engagement lead to higher attrition?")
print("- Do certain departments have higher absenteeism?")
print("- Are high performers more likely to stay?")
