import os
import json
import csv

# Path to the directory containing the JSON files
directory = 'eth'

# Dictionary to store the results
decimals_dict = {}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        # Extract the key from the filename
        key = filename[:-5]  # Remove the '.json' extension
        filepath = os.path.join(directory, filename)
        # Load the JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)
            # Get the 'decimals' field value and ensure it's an int
            decimals = int(data['decimals']) if 'decimals' in data else None
            # Store the key-value pair in the dictionary
            decimals_dict[key] = decimals

# Print the dictionary
# print(decimals_dict)
