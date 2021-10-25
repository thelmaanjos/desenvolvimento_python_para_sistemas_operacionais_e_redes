'''

14. Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.

Tanto psutil.process_iter() quanto o psutil.pids() retornam a lista de processos em execução, porém o psutil.process_iter() é mais eficiente sendo executado repetidamente em iterações (vide seu nome).

'''