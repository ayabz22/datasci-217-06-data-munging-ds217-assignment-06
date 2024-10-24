import pandas as pd
import numpy as np
from scipy import stats

#load the messy data
df = pd.read_csv('messy_population_data.csv') 

#fill the missing values
def fill_nan(df):
    if 'age' in df.columns:
        df['age'].fillna(df['age'].mean(), inplace=True)

    if 'income_groups' in df.columns:
        df['income_groups'].fillna(df['income_groups'].mode()[0], inplace=True)

    if 'gender' in df.columns:
        df['gender'].fillna(df['gender'].mode()[0], inplace=True)
        
    if 'year' in df.columns:
        df['year'].fillna(df['year'].median(), inplace=True)  

    if 'population' in df.columns:
        df['population'].fillna(df['population'].median(), inplace=True)
    return df 

# Remove duplicate rows
def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

#convert to correct data types
def fix_data_types(df):
    df['year'] = df['year'].astype(int)
    df['population'] = df['population'].astype(int)
    df['age'] = df['age'].astype(int)
    df['gender'] = df['gender'].astype('category')
    df['income_groups'] = df['income_groups'].astype('category')
    return df 

# Fix inconsistentcies
def inconsistent_categories(df):
    income_fix = {
        'lower_middle_income_typo': 'lower_middle_income',
        'low_income_typo': 'low_income',
        'high_income_typo': 'high_income',
        'upper_middle_income_typo': 'upper_middle_income',
    }
    df['income_groups'] = df['income_groups'].replace(income_fix)
    df = df[df['gender'] != 3.0] 
    return df

# fix date issue
def remove_future_dates(df):
    future_dates = df[df['year'] > 2024]  # Track future date rows
    df = df[df['year'] <= 2024]
    print("\nFuture Dates Removal Summary:")
    print(f"Number of rows with future dates removed: {len(future_dates)}")
    return df

#remove any outliers
def remove_outliers(df, threshold=3):
    numeric_cols = df.select_dtypes(include=[np.number])  
    z_scores = np.abs(stats.zscore(numeric_cols, nan_policy='omit')) 
    df = df[(z_scores < threshold).all(axis=1)]
    return df

#apply the functions 
def clean_data(df):

    df = fill_nan(df)
    df = remove_duplicates(df)
    df = fix_data_types(df)
    df = inconsistent_categories(df)
    df = remove_future_dates(df)
    df = remove_outliers(df)

    return df

def save_data(df, output_filename):
    df.to_csv(output_filename, index=False)
    print(f"Cleaned data saved to {output_filename}")

def main():
    input_filename = 'messy_population_data.csv'
    output_filename = 'cleaned_population_data.csv'

    df = pd.read_csv(input_filename)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, output_filename)

    # Summary statistics of the cleaned data
    clean_summary = df_cleaned.describe(include='all')
    print("\nSummary statistics for the cleaned data:")
    print(clean_summary)

if __name__ == "__main__":
    main()