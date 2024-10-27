import requests
import pandas as pd
import config

def fetch_gold_data():
    url = f"{config.BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={config.SYMBOL}&interval=5min&apikey={config.API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(response)
    
    time_series = data['Time Series (5min)']
    
    df = pd.DataFrame(time_series).T
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)
    return df
