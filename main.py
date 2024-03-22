import pandas as pd
from stats import trading_stats_dict
from addresses import address_dict

# Assuming trading_stats_dict and address_dict are already populated
merged_dict = {}

for symbol in address_dict.keys():
    if symbol in address_dict:
        # Combine the address, price, and 24hr volume into a list
        merged_dict[symbol] = [address_dict[symbol], trading_stats_dict[symbol]['price'], trading_stats_dict[symbol]['24hr volume']]

# Convert the merged dictionary to a DataFrame
df = pd.DataFrame.from_dict(merged_dict, orient='index', columns=['Address', 'Price', '24hr Volume'])

# Save the DataFrame to a CSV file
df.to_csv('address price 24hr volume by symbol.csv', index_label='Symbol', index=True)
