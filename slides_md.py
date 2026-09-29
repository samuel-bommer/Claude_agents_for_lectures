"""
Convert pdf into md with marktidown.
"""

from markitdown import MarkItDown


md = MarkItDown()
path_cloud = '/Users/sam/Library/Mobile Documents/com~apple~CloudDocs/HSG/'

#path_specific = 'Optimal Decision Making/ODM_week2-1.pdf'
path_specific = 'Steuerrecht/Vorlesung 1.pdf'

path_conc = path_cloud + path_specific
#path_conc = path_specific

result = md.convert(path_conc)
print(result.text_content)

