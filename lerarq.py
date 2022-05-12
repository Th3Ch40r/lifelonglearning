arquivo=input("Digite o nome do arquivo a ser lido: ")
openarq=open(arquivo)

try:
    arquivo=str(arquivo)
    openarq=open(arquivo)
except:
    print("Arquivo não encontrado.")

for texto in openarq:
    print(texto)
