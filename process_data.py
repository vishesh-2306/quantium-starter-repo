import pandas as pd
import glob

# Step 1: Load all CSV files from data folder
files = glob.glob("data/*.csv")
df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Step 2: Combine all into one dataframe
data = pd.concat(df_list, ignore_index=True)

# Step 3: Keep only Pink Morsels
data = data[data['product'] == 'Pink Morsel']

# Step 4: Compute Sales = quantity * price
data['Sales'] = data['quantity'] * data['price']

# Step 5: Keep only required columns
final = data[['Sales', 'date', 'region']]

# Step 6: Save final CSV
final.to_csv("processed_data.csv", index=False)

print("Processing complete. Output file: processed_data.csv")