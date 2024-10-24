
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
    df = df[df['year'] <= 2024] 
    return df

#remove any outliers
def remove_outliers(df, threshold=3):
    numeric_cols = df.select_dtypes(include=[np.number])  
    z_scores = np.abs(stats.zscore(numeric_cols, nan_policy='omit')) 
    df = df[(z_scores < threshold).all(axis=1)]
    return df

