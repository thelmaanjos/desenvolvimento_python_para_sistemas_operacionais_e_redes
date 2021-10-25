import os

'''
4. Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório com caminho relativo? Dê um exemplo.

O comando os.path.abspath(file) retorna o caminho absoluto de um arquivo, em que "path" é o caminho relativo.

'''
path = 'thelma_q4.py'
print(path)
print(os.path.abspath(path))