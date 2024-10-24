# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis 

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125,718
- **Columns**: 5

### Column Details

| Column Name     | Data Type | Non-Null Count | Unique Values | Mean           |
|-----------------|-----------|----------------|---------------|----------------|
| income_groups   | object    | 119,412        | 8             | N/A            |
| age             | float     | 119,495        | 101           | 50.001         |
| gender          | float     | 119,811        | 3             | N/A            |
| year            | object    | 125,718        | 170           | N/A            |
| population      | object    | 125,718        | 114926        | 1.579          |

### Identified Issues

1. **Missing Values**
   - Description: There are missing values as NaN
   - Affected Column(s): income groups (6306), age (6223), gender (5907)
   - Example: Row 6306 has NaN in income_groups, Row 6223 has a NaN in age
   - Potential Impact: If left uncleaned they can affect our conclusions because it can result in a  
     skew 

2. **Duplicates**
   - Description: there are 2950 duplicate rows
   - Affected Column(s): All columns 
   - Potential impact: duplicate rows may over represent which can affect our conclusions thus they  
     need to be removed

3. **Data Types**
   - Description: Some of the data types are incorrect 
   - Affected Column(s): All columns
   - Example: Age is a float but should ideally be integer, and gender is a float which should ideally 
     be catgeorical and year is an object but should be integer and population is object and should be integer
   - Potential Impact: If left uncleaned they can affect our conclusions because it can result in a  
     skew 

4. **Inconsistent Values**
   - Description: There are typos and unexpected values
   - Affected Column(s): income_groups and gender
   - Example: Income_groups has typose like upper_middle_income_typo and gender column has values like 
     3.0
   - Potential Impact: If left uncleaned they can lead to unclear data

5. **Date Issues**
   - Description: There are some years that are way past 2024
   - Affected Column(s): years
   - Example: I saw some 2111, 2115, 2108, etc. 
   - Potential Impact: These dates that are in the future can skew the data 

6. **Outliers**
   - Description: Check through dataset for outliers through the z-score method, none were found
   - Affected Column(s): None
   - Example: Since there was none, theres no examples 
   - Potential Impact: If there were outliers, it can also skew the data and impact our results thus 
     they need to be removed if present 


## 2. Data Cleaning Process

### Issue 1: Missing Values
- **Cleaning Method**: Handle missing values by filling them with their mean or mode 
- **Implementation**:
    ```python
    if 'age' in df.columns:
        df['age'].fillna(df['age'].mean(), inplace=True)
    ```
- **Justification**: Filling missing values in `age` with the mean ensures that we don’t lose too much data and the missing spot is acctually filled and not empty. This is also better than just removing them. 

- **Impact**: Minimal change in distribution as filling is done with mean values.


### Issue 2: Duplicated Rows

- **Cleaning Method**: use the `drop_duplicates()` function to remove all duplicated rows in the dataset
- **Implementation**:
    ```python
    df_messy_cleaned = df_messy.drop_duplicates()
    ```
-**Justification**: Duplicates need to be removed because they are not necessary and only will skew the data and lead to misleading conclusions. 

-**Impact**: 2950 rows were deleted.  


### Issue 3: Data Types 

- **Cleaning Method**: use the `as.type()` function to convert the variables to the correct type. So I converted all of them to the correct one. 
- **Implementation**:
    ```python
    df['year'] = df['year'].astype(int)
    ```
-**Justification**: If we don't have the correct data type this will mess up our analysis. 

-**Impact**: Now the variables are in their correct data type. 

### Issue 4: Inconsistent Values 

- **Cleaning Method**: use the `replace()` function to replace it with the correct value
- **Implementation**:
    ```python
    df['income_groups'] = df['income_groups'].replace(income_fix)
    ```
-**Justification**: This ensures that our dataset is consistent and readable to the audience thus those typos had to be replaced

-**Impact**: This affected the gender and income_groups column as the typo got replaced with the correct income group and 3s were removed. 

### Issue 5: Date Issues

- **Cleaning Method**: I created a simple function that exludes any dates that are higher than 2024 
- **Implementation**:
    ```python
    df = df[df['year'] <= 2024]
    ```
-**Justification**: This ensures that our dataset is consistent with the present time and doesnt have future dates

-**Impact**: Because of this several rows were removed 

### Issue 6: Outliers

- **Cleaning Method**: I created a simple function identifies outliers and removes them using the z score method 
- **Implementation**:
    ```python
    z_scores = np.abs(stats.zscore(numeric_cols, nan_policy='omit'))
    ```
-**Justification**: This ensures that our dataset is doesn't have any outliers

-**Impact**: Since there was no outliers, nothing changed. 

