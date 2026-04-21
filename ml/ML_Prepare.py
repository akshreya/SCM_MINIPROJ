import pandas as pd

def prepare_data():
    # load dataset
    df = pd.read_csv("../dataset/orders_cleaned.csv")

    # convert date
    df['order_date'] = pd.to_datetime(df['order_date'])

    # sort
    df = df.sort_values('order_date')

    # group by date (daily demand)
    daily = df.groupby('order_date')['quantity'].sum().reset_index()

    # convert date to numeric
    daily['days'] = (daily['order_date'] - daily['order_date'].min()).dt.days

    return daily
