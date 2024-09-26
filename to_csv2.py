import pandas as pd

# Path to the JSON file
json_file = '/home/ashkan/Code/testimonial_llm_analysis/data/data_final.json'

# Read the JSON file into a pandas DataFrame
df = pd.read_json(json_file)

# Path to save the CSV file
csv_file = '/home/ashkan/Code/testimonial_llm_analysis/data/data_final.csv'

# Convert the DataFrame to CSV format and save it
df.to_csv(csv_file, index=False)