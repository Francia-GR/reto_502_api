import json
import pandas as pd

from fastapi import FastAPI, UploadFile
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

from app.dependencies import binary_to_dataframe, group_dataframe
from app.model import get_predictions

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Upload files for prediction."}

@app.post("/uploadfile/predict_{aggregation_freq}")
async def create_upload_file(file: UploadFile, aggregation_freq: str, num_of_predictions: int):

    # Reading JSON file as a binary string.
    binary_string = await file.read()

    # Transforming binary to dataframe with date | data columns.
    time_series = binary_to_dataframe(binary_string)

    time_series_grouped = group_dataframe(time_series, aggregation_freq)

    # Getting predictions.
    pred = get_predictions(time_series_grouped, num_of_predictions).to_dict()
    
    return pred


