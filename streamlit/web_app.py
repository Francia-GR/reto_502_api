import requests
import pandas as pd
import streamlit as st

def post_request(aggregation, num_of_predictions):
    '''
    Args:
        None

    Returns:
        data [dictionary] : Response from the API (JSON like response)

    '''

    # Define the API endpoint URL
    url = f'http://127.0.0.1:8000/uploadfile/predict_{aggregation}'
    files = {'file': open('streamlit/data.json' ,'rb')}
    params = {"num_of_predictions": num_of_predictions}

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.post(url, files=files, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
  
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None


data_columns = ["Company 1", "Company 2", "Company 3"]

st.title('Income Forecast')
st.write('Web app demo interacting with API for time series prediction.')

company = st.selectbox('Company',
                        data_columns)

agg_options = {'By day':'daily', 'By week':'weekly', 'By month':'monthly'}

aggregation = st.selectbox('Compute predicions:',
                           agg_options.keys())
aggregation = agg_options[aggregation]

num_of_predictions = st.number_input("Enter an integer number", step=1, format="%d")

posts = post_request('weekly', 5)
if posts:
    print(type(posts))
    print(posts)
else:
    print('Failed to fetch data from API.')