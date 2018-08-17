""" Lê um arquivo de texto
INPUT:
Entra com o cominho do arquivo a ser lido
""" 
f = open('/Users/thiagocarvalho/Documents/GitHub/dataScience1/data/some_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()

""" Escreve um arquivo de texto
INPUT:
Entra com o cominho do arquivo a ser escrito
""" 
f = open('/Users/thiagocarvalho/Documents/GitHub/dataScience1/data/my_file.txt', 'w')
f.write("Hello there!")
f.close()

""" Verifica o máximo de arquivos que podem ser abertos
INPUT:
Lista
""" 
files = []
for i in range(10000):
    files.append(open('/Users/thiagocarvalho/Documents/GitHub/dataScience1/data/some_file.txt', 'r'))
    print(i)

""" Ler e fechar o arquivo automaticamnete """
with open('/Users/thiagocarvalho/Documents/GitHub/dataScience1/data/my_file.txt', 'r') as f:
    file_data = f.read()