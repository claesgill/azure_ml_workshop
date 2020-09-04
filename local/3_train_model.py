import pandas as pd

# Get data

df = pd.read_csv('data/08.csv')
# for column in df.columns:
#     print(column)

unique = set(df['start_station_id'])
print(unique)
print(len(unique))



# Preprosses as needed

# Train and evaluate model

# Save model

