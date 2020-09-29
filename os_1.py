''' OS Module '''
#https://docs.python.org/3/library/os.html
#https://www.youtube.com/watch?v=tJxcKyFMTGo
#O módulo OS nos permite interagir com o sistema operacional subjacente de várias maneiras diferentes.

import os #built-in module - not necessary to install any third-party libraries
from datetime import datetime

#print(dir(os)) #shows all of the attributes and methods that we have access

#os.chdir('C:\\Users\\user\\Documents\\Python\\Python Corey\\os')
#print(os.getcwd())

#lista os diretórios
#print(os.listdir())

#creates a folder
#os.mkdir('os_test') #just creates a directory
#os.makedirs('os_test1/os_sub') #creates all of the intermediate level directories that you need
#print(os.listdir())

#removes a folder
#os.rmdir('os_test')
#os.removedirs('os_test1/os_sub')
#print(os.listdir())

#rename
#os.rename('test.txt', 'demo.txt') #pass in the original file name first
#print(os.listdir())

#lista informações sobre o arquivo de texto
##print(os.stat('test.txt'))

#traz o tamanho do arquivo
#print(os.stat('test.txt').st_size)

#traz o tempo de modificação em timestamp humano
#mod_time = os.stat('test.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))

'''
#creates an entire tree of all directories and files
os.chdir('C:\\Users\\user\\Desktop\\')

for dirpath, dirnames, filenames in os.walk('/Users/user/Documents/Python/Python Corey'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

'''
os.chdir('C:/Users/user/Documents/Python/Python Corey')
#print(os.environ.get('home'))

#une dois paths (muito útil, e substitui o '+' ao unir dois paths)
#file_path = os.path.join(os.environ.get('Python Corey'), 'test.txt')
#print(file_path)

#prints the basename of the file
#print(os.path.basename('/tmp/text.txt'))

#prints the directory name of the file
#print(os.path.dirname('/tmp/text.txt'))

#prints the directory and basename of the file
#print(os.path.split('/tmp/text.txt'))

#verifica se o arquivo existe (não existe pq não criei)
#print(os.path.exists('/tmp/text.txt'))

#verifica se é um diretório
#print(os.path.isdir('/tmb/morango'))

#verifica se é um arquivo
#print(os.path.isfile('/tmb/morango'))

#split the file root and extension
#print(os.path.splitext('/tmb/test.txt'))

#if you want to see everything that is available within os.path:
print(dir(os.path))
