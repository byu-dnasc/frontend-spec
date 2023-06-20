import json
from tabulate import tabulate

file_name = 'movie'

# Read data from JSON file
with open(f'json/model/{file_name}.json') as file:
    data = json.load(file)

table_data = []
for property_name, item in data['properties'].items():
    # extact column name and pop-up window name, if present
    popup_name = ''
    if 'pop-up window' in item.keys():
        # if no pop-up window, print n/a
        popup_name = 'n/a'
        if item['pop-up window'] != '':
            popup_name = item['pop-up window']
            # capitalize words that are not property names
            title_name = [word.title() if word not in data['properties'].keys() else word for word in popup_name.split(' ')]
            popup_name = ' '.join(title_name)
    column_name = ''
    if 'column name' in item.keys():
        column_name = item['column name'].title()
    table_data.append([column_name, property_name, popup_name])

# Generate LaTeX code for the table
headers = ["Column Name", "Property Name", "Pop-up Window"]
table_code = tabulate(table_data, headers=headers, tablefmt='latex_booktabs')

table_code = table_code.replace(r'{tabular}', r'{tabularx}', 2)
table_code = table_code.replace(r'{lll}', r'{\textwidth}{l|l|X}', 1)

# enclose all property names in \texttt{}
for property_name in data['properties'].keys():
    property_name = property_name.replace('_', '\_')
    table_code = table_code.replace(property_name, r'\texttt{' + property_name + r'}')

# Write the LaTeX code to a file
with open(f'table/{file_name}_view.tex', 'w') as file:
    file.write(table_code)