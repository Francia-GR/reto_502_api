import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def get_predictions(series, n_predictions):
    '''
    Args:
        series [pd.DataFrame]: 'date' and 'data' columns.'date' values 
                                should be in pd.datetime format.
        n_predictions [int]: Number of predictions to compute.

    Returns:
        forecast_df [pd.DataFrame] : With 'date' and 'data' columns 
                                     containing next n predictions.
    '''
    series.set_index('date', inplace=True)

    model = ARIMA(series['data'], order=(5, 1, 0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=n_predictions)
    forecast_df = pd.DataFrame({'forecast': forecast})

    # forecast_df['date'] = forecast_df.index
    # forecast_df.reset_index(inplace = True, drop = True)

    # Generate next dates
    # ...

    return forecast_df