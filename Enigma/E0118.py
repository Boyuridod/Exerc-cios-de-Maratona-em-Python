mensagem = list(input())
crib = list(input())

cont = x = 0
y = len(crib)

for i in range(len(mensagem) - len(crib)):
    certo = False
    for j in range(y):
        if(mensagem[i + j] == crib[j]):
            
    if(certo):
        cont += 1