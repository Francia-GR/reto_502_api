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
    url = f'http://127.0.0.1:8000/uploadfile/predict_{aggregation}'#?num_of_predictions={num_of_predictions}'
    files = {'file': open('data.json' ,'rb')}
    params = {"num_of_predictions": num_of_predictions}

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.post(url, files=files, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(type(response))
            print(response)
            data = response.json()
            return data
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
  
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None

'''    
def main():

    posts = post_request('weekly', 1)
    if posts:
        print(type(posts))
        print(posts)
    else:
        print('Failed to fetch data from API.')

if __name__ == '__main__':
    main()
'''    

data_columns = ["Email", "Home phone", "Mobile phone"]

st.title('Income Forecast')
st.write('Web app demo interacting with API for time series prediction.')

company = st.selectbox('Company',
                        data_columns)
aggregation = st.selectbox('Compute predicions:',
                           ['daily', 'weekly', 'biweekly', 'monthly'])