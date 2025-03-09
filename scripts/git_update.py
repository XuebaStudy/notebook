import os

kind = 'test'
order = '8.4'

name = kind+order

os.system('git add .')
com =''.join(['git commit -m ',name])
os.system(com)
os.system('git push -u origin main')
os.system('mkdocs gh-deploy')
