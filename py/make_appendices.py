import os

# for each appendix in appendix/, add the appendix to the appendices.tex file
with open('appendices.tex', 'w') as file:
    for filename in os.listdir('appendix'):
        appendix = filename.split('.')[0]
        label = appendix.replace('_', '')
        appendix = appendix.replace('_', ' ')
        appendix = appendix.title()
        tex_code = r'\chapter{%s\label{appendix:%s}}' % (appendix, label) + '\n' \
                   r'\input{appendix/%s}' % filename + '\n'
        file.write(tex_code)