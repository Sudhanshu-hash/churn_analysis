import pandas as pd

# Load,Preview and print dataset structure
df = pd.read_csv("Telco_Customer_Churn_data.csv")
print(df.head())
print(df.info())

# Shape and columns
print("Shape:", df.shape)
print("Columns:", df.columns)


# Convert TotalCharges to numeric ( errors='coerce' fix incorrect datatype)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check missing values after conversion
print("Missing values:\n", df.isnull().sum())

# Drop rows with missing TotalCharges
df = df.dropna(subset=['TotalCharges'])

# Check & Remove duplicates
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Convert target variable to numeric
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df.info()
print(df.isnull().sum())

print("\n--- DATA CLEANING COMPLETED ---\n")


# Analysis (EDA)

# Calculate churn rate
churn_rate = df['Churn'].mean()
print("Churn Rate:", churn_rate)
# Group by tenure and calculate churn
tenure_churn = df.groupby('tenure')['Churn'].mean()
print(tenure_churn.head(6))

# Churn by contract type
contract_churn = df.groupby('Contract')['Churn'].mean()
print(contract_churn)

# Average monthly charges by churn
charges_churn = df.groupby('Churn')['MonthlyCharges'].mean()
print(charges_churn)

payment_churn = df.groupby('PaymentMethod')['Churn'].mean()
print(payment_churn)

cleaned_file_name = "churn_cleaned_data.csv"
df.to_csv(cleaned_file_name, index=False)
print(f"Cleaned dataset saved as {cleaned_file_name}")