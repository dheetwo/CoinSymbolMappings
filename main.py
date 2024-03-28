import pandas as pd
from stats import trading_stats_dict
from addresses import address_dict
from decimals import decimals_dict

# Assuming trading_stats_dict and address_dict are already populated
merged_dict = {}

for symbol in address_dict.keys():
    if symbol in address_dict:
        # Combine the address, price, and 24hr volume into a list
        merged_dict[symbol] = [address_dict[symbol], trading_stats_dict[symbol]['price'], trading_stats_dict[symbol]['24hr volume']]

# Convert the merged dictionary to a DataFrame
df = pd.DataFrame.from_dict(merged_dict, orient='index', columns=['Address', 'Price', '24hr Volume'])

# Create a new column 'Decimals' and initialize it with 'address not found'
df['Decimals'] = 'address not found'

# Update 'Decimals' column with decimals values if address matches
for index, row in df.iterrows():
    address = row['Address']
    if address in decimals_dict:
        df.at[index, 'Decimals'] = decimals_dict[address]

# print(df)

# Save the DataFrame to a CSV file
df.to_csv('address price 24hr volume decimals by symbol.csv', index_label='Symbol', index=True)
