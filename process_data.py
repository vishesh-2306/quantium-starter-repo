import pandas as pd
import glob

# Load all CSV files from data folder
files = glob.glob("data/*.csv")
df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

data = pd.concat(df_list, ignore_index=True)


data = data[data['product'].str.lower() == 'pink morsel']


data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)


data['Sales'] = data['quantity'] * data['price']


final = data[['Sales', 'date', 'region']]


final['region'] = final['region'].str.lower()


final.to_csv("processed_data.csv", index=False)

print("Processing complete! Rows:", final.shape[0])
