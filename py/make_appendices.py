import os

# for each appendix in appendix/, add the appendix to the appendices.tex file
with open('appendices.tex', 'w') as file:
    filenames = [f for f in os.listdir('appendix') if os.path.isfile(f'{os.getcwd()}/appendix/{f}')]
    for filename in filenames:
        appendix = filename.split('.')[0]
        label = appendix.replace('_', '')
        appendix = appendix.replace('_', ' ')
        appendix = appendix.title()
        tex_code = r'\chapter{%s\label{appendix:%s}}' % (appendix, label) + '\n' \
                   r'\input{appendix/%s}' % filename + '\n'
        file.write(tex_code)