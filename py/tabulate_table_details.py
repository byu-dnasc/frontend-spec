import json
from tabulate import tabulate

def tabulate_table_details(file_name):

    # Read data from JSON file
    with open(f'json/model/{file_name}.json') as file:
        data = json.load(file)

    table_data = []
    for property_name, item in data['properties'].items():
        if 'in_table' not in item.keys():
            continue
        # extact column name and pop-up window name, if present
        popup_name = 'n/a'
        if 'pop-up window' in item.keys():
            popup_name = item['pop-up window']
            # capitalize words that are not property names
            title_name = [word.title() if word not in data['properties'].keys() else word for word in popup_name.split(' ')]
            popup_name = ' '.join(title_name)
        column_name = item['name'].title()
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
    with open(f'table/{file_name}_table_details.tex', 'w') as file:
        file.write(table_code)

table_names = ['movie']

# generate LaTeX table file for each model
for name in table_names:
    tabulate_table_details(name)
