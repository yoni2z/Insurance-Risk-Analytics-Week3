import pandas as pd

df = pd.read_csv('data/MachineLearningRating_v3.csv')
df['VehicleAge'] = pd.to_datetime('2025-06-18').year - df['RegistrationYear']
df.to_csv('data/MachineLearningRating_v3_v2.csv', index=False)