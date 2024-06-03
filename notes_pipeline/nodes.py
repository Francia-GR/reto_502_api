import pandas as pd
import numpy as np

def load_data(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Retrive data from DB and standarize names of columns.
    Create pivot table to get time series by company ID.

    Args:
        None

    Returns:
        pivot_data [pd.DataFrame]: Dataframe containing time series by company_id.
    '''
    
    data = data.drop(data.columns[0], axis=1)
    data.columns = ['date', 'company', 'data']
    data['date'] = pd.to_datetime(data['date'])

    pivot_data = data.pivot(index='date', columns='company', values='data')
    pivot_data.columns = [f'company_{col}' for col in pivot_data.columns]
    pivot_data.reset_index(inplace=True)

    return pivot_data

def fill_missing_dates(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Creates empty rows for dates that are missing in the time series.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the date column and a columns for each company ID.
        date_column (str): Name of the column containing the dates.
    
    Returns:
        pd.DataFrame: DataFrame with missing dates filled with null values.
    '''

    date_column = 'date'
    
    # Ensure the date column is in datetime format
    data[date_column] = pd.to_datetime(data[date_column])
    
    # Set the date column as the index
    data.set_index(date_column, inplace=True)
    
    # Create a complete date range from the min to the max date in the DataFrame
    complete_date_range = pd.date_range(start=data.index.min(), end=data.index.max(), freq='D')
    
    # Reindex the DataFrame to this complete date range
    df_reindexed = data.reindex(complete_date_range)
    
    # Rename the index back to the original date column name
    df_reindexed.index.name = date_column
    
    # Reset index to convert the date index back to a column
    df_reindexed.reset_index(inplace=True)
    
    return df_reindexed

def handle_outliers(dataframe:pd.DataFrame) -> pd.DataFrame:
    '''
    Identify and handle outliers.
    Replaces outliers by zero to be treated like missing values.

    Args:
        dataframe [pd.DataFrame]: Columns 'date' and one for each company ID
                                  as independent time series.


    Returns:
        [pd.DataFrame]: Same columns, outliers replaced by NaN values.


    '''
    for column in dataframe.columns:
        if column != 'date':
            # Calculate Q1 (25th percentile) and Q3 (75th percentile) for the current time series column
            Q1 = dataframe[column].quantile(0.25)
            Q3 = dataframe[column].quantile(0.75)
            IQR = Q3 - Q1  # Interquartile range

            # Define lower and upper bounds for outliers
            lower_bound = Q1 - 3 * IQR
            upper_bound = Q3 + 3* IQR

            # Replace outliers with NaN in the current column
            dataframe[column] = dataframe[column].apply(lambda x: x if lower_bound <= x <= upper_bound else np.nan)
    
    return dataframe



def fill_missing_data(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Fill missing data for each company's time series.

    Args:
        dataframe [pd.DataFrame]: Columns 'date' and one for each company ID
                                  as independent time series.

    Returns:
        [pd.DataFrame]: Same columns, missing data filled.
    '''
    # Create a copy of the data to avoid modifying the original dataframe
    filled_data = data.copy()

    # Iterate over each column except the 'date' column
    for column in filled_data.columns:
        if column != 'date':
            # Calculate the mean of the series, ignoring NaNs
            mean_value = filled_data[column].mean()
            
            # Fill NaN values with the mean value
            filled_data[column] = filled_data[column].fillna(mean_value)
        
    return filled_data

    



