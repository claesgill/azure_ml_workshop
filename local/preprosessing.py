import pandas as pd


data_df = pd.read_csv('data/08.csv')

data_df['started_at'] = pd.to_datetime(data_df['started_at'])

data_df['hour']    = data_df['started_at'].dt.hour
data_df['day']     = data_df['started_at'].dt.day
data_df['day_of_week'] = data_df['started_at'].dt.weekday
data_df['weekend'] = pd.to_numeric(data_df['day_of_week'] >= 5).astype(int)
data_df['week']    = data_df['started_at'].dt.week
data_df['month']   = data_df['started_at'].dt.month
data_df['year']    = data_df['started_at'].dt.year

print(data_df.head())

print(data_df[data_df['hour'] == 0 ].shape)