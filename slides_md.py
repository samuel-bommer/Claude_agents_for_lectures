"""
Convert pdf into md with marktidown.
"""

from markitdown import MarkItDown


md = MarkItDown()
path_cloud = '/Users/sam/Library/Mobile Documents/com~apple~CloudDocs/HSG/'

#path_specific = 'Macro III/Exercises/MTDS24_Exam.pdf'
path_specific = 'Optimal Decision Making/ODM_week1-3.pdf'
#path_specific = '/Users/sam/Downloads/finance_report_Roche.pdf'

path_conc = path_cloud + path_specific
#path_conc = path_specific

result = md.convert(path_conc)
print(result.text_content)

