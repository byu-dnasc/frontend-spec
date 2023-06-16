import json

with open('json/urls.json') as file:
    urls = json.load(file)

newcommands = []
for name, url in urls.items():
    # escape underscores
    url = url.replace('_', r'\_')
    # escape pound signs
    url = url.replace('#', r'\#')
    newcommands.append(r'\newcommand{\link%s}[1]{\href{%s}{\uline{#1}}}' % (name, url))

with open('links.tex', 'w') as file:
    file.write('\n'.join(newcommands))