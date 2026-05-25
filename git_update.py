import os

message = 'update'


os.system('git add .')
com =''.join(['git commit -m "',message,'"'])
os.system(com)
os.system('git push -u origin main')
os.system('mkdocs gh-deploy')
