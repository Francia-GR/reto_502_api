import pandas as pd

def load_data() -> pd.DataFrame:
    '''
    Retrive data from DB and standarize names of columns.
    Create pivot talbe to get time series by company ID.
    '''
    pass

def fill_missing_dates(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Creates empty rows for dates that are missing in the time series.
    '''
    pass

def handle_outliers(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Identify and eliminate outliers (replace by NaN).
    '''
    pass


def fill_missing_data(data:pd.DataFrame) -> pd.DataFrame:
    '''
    Fill missing data for each company's time series. 
    Returns list of 6 dataframes.
    '''


