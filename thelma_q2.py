import os

'''
2. Sobre variáveis de ambiente, responda:

a) O que são?

Variáveis que guardam um valor disponível no ambiente que um processo executa. Esse valor pode ser, por exemplo, o caminho para o local de arquivos temporários, o caminho para o binário do Java, pode ser o nome do usuário logado, pode ser informações do processador... Existem vários tipos de variáveis com seus respectivos valores, muitos criados dinamicamente e gerenciado pelo sistema operacional. Eles existem para facilitar que o processo encontre o caminho ou a informação correta daquilo que ele procura, porque muitos dos valores das variávels muda de sistema operacional para sistema operacional, ou até de versão de um programa para versão do mesmo programa.

Ref: https://cursos.alura.com.br/forum/topico-oque-e-afinal-de-contas-a-variavel-de-ambiente-39421
https://pt.wikipedia.org/wiki/Vari%C3%A1vel_de_ambiente

b) Como elas podem ser obtidas pelo módulo ‘os’ de Python?

Executando os.environ, ou print(os.environ) para printá-las. O output será um dicionário com chave (nome da variável) e valor de cada uma delas 

c) Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?

Acessando através da chave. Por exemplo: 
print(os.environ['HOMEDRIVE'])

'''

print(os.environ)
print(os.environ['HOMEPATH'])