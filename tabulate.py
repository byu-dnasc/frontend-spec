import json
import tabulate

# Read data from JSON file
with open('data.json') as file:
    data = json.load(file)

# Extract header values from JSON
headers = data['headers']

# Extract the table data from the JSON
table_data = []
for row in data['rows']:
    table_data.append([row[column_name] for column_name in headers])

# Generate LaTeX code for the table
table_code = tabulate(table_data, headers=headers, tablefmt='latex')

# Write the LaTeX code to a file
with open('table.tex', 'w') as file:
    file.write(table_code)
