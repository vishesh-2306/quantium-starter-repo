import pandas as pd
import glob


files = glob.glob("data/*.csv")
df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)


data = pd.concat(df_list, ignore_index=True)


data = data[data['product'] == 'Pink Morsel']


data['Sales'] = data['quantity'] * data['price']


final = data[['Sales', 'date', 'region']]


final.to_csv("processed_data.csv", index=False)

print("Processing complete. Output file: processed_data.csv")