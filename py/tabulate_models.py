################################
# This script reads in JSON models and generates LaTeX code for a table
#
#
import json
import os
from tabulate import tabulate

def latex_quotes(string):
    modified_string = ''
    quotes_count = 0

    for char in string:
        if char == '"':
            if quotes_count % 2 == 0:
                modified_string += '``'
            else:
                modified_string += "''"
            quotes_count += 1
        else:
            modified_string += char

    return modified_string

def tabulate_json(model_name):

    # Read data from JSON file
    with open(f'json/model/{model_name}.json') as file:
        data = json.load(file)

    # extract property names and descriptions from JSON
    table_data = []
    for property_name, item in data['properties'].items():
        description = item['description']
        # Convert any double quotes to LaTeX quotes
        if type(description) == str:
            description = latex_quotes(description)
        table_data.append([property_name, description])

    # Generate LaTeX code for the table
    headers = ["Property Name", "Description"]
    table_code = tabulate(table_data, headers=headers, tablefmt='latex')

    # allow line wrapping in the second column
    table_code = table_code.replace(r'{tabular}', r'{tabularx}', 2)
    table_code = table_code.replace(r'{ll}', r'{\textwidth}{l|X}', 1)

    # enclose all property names in \texttt{}
    for property_name in data['properties'].keys():
        property_name = property_name.replace('_', '\_')
        table_code = table_code.replace(property_name, r'\texttt{' + property_name + r'}')

    # Write the LaTeX code to a file
    with open(f'table/{model_name}_model.tex', 'w') as file:
        file.write(table_code)

# collect model names from json/model
model_names = [file.split('.')[0] for file in os.listdir('json/model')]

# generate LaTeX table file for each model
for model_name in model_names:
    tabulate_json(model_name)
