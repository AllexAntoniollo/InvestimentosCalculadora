from classes.Conta import Conta
import matplotlib.pyplot as plt
from itertools import combinations_with_replacement

cotacao = float(input("Qual a cotação da Posi? "))
saldoaplicado = float(input("Quantas Posis você tem aplicado? "))
apr = float(input("Qual o apr diario? "))
dias = int(input("Quantos dias? "))


Conta = Conta(saldoaplicado,saldoaplicado,apr,cotacao,dias)

Conta.setCotacao(cotacao)
Conta.setSaldoAplicado(saldoaplicado)
Conta.setApr(apr)
Conta.setDias(dias)


#for x in range(100):
#    x += 1
#    Conta.sacar(x)
#    Conta.setSaldoAplicado(saldoaplicado)
#    dicio[x] = round(Conta.getPosi(), 2)

lista = [0]
for i in range(Conta.dias):
    i += 1
    lista.append(i)

perm = combinations_with_replacement(lista, Conta.dias)
list2 = []
for comb in perm:
    if (sum(comb) <= Conta.dias):
        listagem = list(comb)
        listagem = list(filter((0).__ne__, listagem))
        list2.append(listagem)
dicio = Conta.sacar(list2)

y = dicio[1][0]
x = dicio[0]
print(dicio[0])
print(dicio[1][0])



plt.plot(x, y, label='Reinvestimento',color="g")
plt.ylabel('Valor em Posi na carteira')
plt.xlabel('Dias para reinvestir')
plt.title('Position reinvestimento')
plt.legend()
plt.show()





