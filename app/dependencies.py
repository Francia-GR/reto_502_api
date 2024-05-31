import json
import pandas as pd

def binary_to_dataframe(binary_string):
    '''
    Args:
        binary string [string]

    Returns:
        dataframe [pd.DataFrame] : 'date' and 'data' columns.
    '''
    # Binary String >> JSON string >> dictionary (list of json objects) >> dataframe
    json_string = binary_string.decode('utf-8')
    data =  json.loads(json_string)
    dataframe = pd.DataFrame(data)

    # Change name columns of data
    # ...

    # Unix Timestamps to pd.datetime
    dataframe['date'] = pd.to_datetime(dataframe['date'], unit='ms')
    
    return dataframe



def group_dataframe(dataframe, freq):
    '''
    Args:
        dataframe [pd.DataFrame]: Includes date and data columns
        frequency [string]: String that describes the frequency of aggregation.
                            Can be 'daily', 'weekly', 'biweekly', 'monthly'
    Returns:
        grouped_df [pd.DataFrame] : Gropued dataframe with date an data columns.                                      
    '''

    frequencies = {'daily':'D',
            'weekly':'W',
            'biweekly':'2W',
            'monthly':'M'}

    grouped_df = dataframe.resample(frequencies[freq], on='date').sum()
    grouped_df.drop(index=grouped_df.index[-1], axis=0, inplace=True)
    grouped_df['date'] = grouped_df.index
    grouped_df.reset_index(drop=True, inplace=True)

    return grouped_df[['date', 'data']]