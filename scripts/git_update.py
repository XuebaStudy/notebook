import os

kind = 'Date'

year_month = ' 2025.4.'
date = '19'
message = ' '


name = kind + year_month + date + message

os.system('git add .')
com =''.join(['git commit -m "',name,'"'])
os.system(com)
os.system('git push -u origin main')
os.system('mkdocs gh-deploy')
