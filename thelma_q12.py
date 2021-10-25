'''

12) Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada.

'''

################### utilizando subprocess com subprocess.Popen()

import subprocess

# Cria um processo e retorna imediatamente ao pai (sem esperar) um objeto com diversos atributos e funções acessíveis
p = subprocess.Popen("calc")
print("PID do processo criado:", p.pid)

################### utilizando os com os.startfile() e os.system()

import os

# Inicia um processo sem retornar a quem chama (pai)
# Processo pai perde o controle do processo
executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
os.startfile(executavel_com_path)
print("Fora do controle do processo pai")

# Espera terminar a execução do processo criado
# Retorna ao pai
os.system("calc")
print("Controle do processo pai")