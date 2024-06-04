import requests
import pandas as pd
import streamlit as st

def post_request(url, files, params):
    '''
    Args:
        None

    Returns:
        data [dictionary] : Response from the API (JSON like response)

    '''
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


# Web App
# --------------------------------------------------------------------------   

st.title('Income Forecast')
st.write('Web app demo interacting with API for time series prediction.')

# Input Parameters
# --------------------------------------------------------------------------   

company = st.selectbox('Company',
                        ["Company 1", "Company 2", "Company 3"])

agg_options = {'By day':'daily', 'By week':'weekly', 'By month':'monthly'}

aggregation = st.selectbox('Compute predicions:',
                           agg_options.keys())
aggregation = agg_options[aggregation]

num_of_predictions = st.number_input("Enter an integer number", step=1, format="%d")


# API Endpoint
# --------------------------------------------------------------------------   

url = f'http://127.0.0.1:8000/uploadfile/predict_{aggregation}'
files = {'file': open('streamlit/data.json' ,'rb')}
params = {"num_of_predictions": num_of_predictions}


# API Call
# --------------------------------------------------------------------------   

if st.button('Compute Predictions'):
    results = post_request(url, files, params)
    # print(results)
    if results:
        output_data = pd.DataFrame(list(results['forecast'].items()), 
                                   columns=['Date', 'Forecast'])

        st.dataframe(output_data, hide_index=True, use_container_width=True)
    else:
        print('Failed to fetch data from API.')