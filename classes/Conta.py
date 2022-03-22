import operator
class Conta:
    def __init__(self, saldoAplicado,saldoInicial, apr,cotacao,dias):
        self.saldo = 0.00
        self.saldoInicial = saldoInicial
        self.saldoAplicado = saldoAplicado
        self.apr = apr
        self.cotacao = cotacao
        self.dias = dias

    def setDias(self, dias):
        self.dias = dias

    def setSaldoAplicado(self, saldoAplicado):
        self.saldoAplicado = saldoAplicado * self.cotacao

    def setApr(self, apr):
        self.apr = apr / 100

    def setCotacao(self, cotacao):
        self.cotacao = cotacao

    #def sacar(self, diasInvestir):
    #    numero = 100 / diasInvestir
    #    numeroInteiro = int(numero)
    #    diferença = numero - numeroInteiro
    #    dias = diferença * 100 / numero

    #    for x in range(numeroInteiro):
    #        saque = self.saldoAplicado * diasInvestir * self.apr
    #        self.saldo = self.saldo + saque -1
    #        self.investir()

    #        saldoSaque = int(dias) * self.apr * self.saldoAplicado
    #        self.posi = saldoSaque + self.saldoAplicado

    def sacar(self,combinacoes):
        lista_Pronta = []
        id = 0
        for lista in combinacoes:
            lista_Valores = []
            agrupamento = []
            lista_dias = list(lista)
            lista_dias.append(0)
            lista_dias = lista_dias[::-1]
            agrupamento.append(lista_dias)

            self.saldoAplicado = self.saldoInicial

            lista_Sub = [self.saldoInicial]
            for dia in lista_dias:
                if(dia != 0):
                    saque = dia * self.apr * self.saldoAplicado
                    self.saldo += saque - 1
                    self.investir()
                    lista_Sub.append(round(self.saldoAplicado,2))

            lista_Valores.append(lista_Sub)

            if(sum(lista_dias) != self.dias):
                diferenca = self.dias - sum(lista_dias)
                variavel = diferenca * self.apr * self.saldoAplicado
                lista_Valores[-1][-1] += variavel

            agrupamento.append(lista_Valores)

            lista_Pronta.append(agrupamento)
        maiores = []
        for valor in lista_Pronta:
            maximo = max(valor[1][0])
            maiores.append(maximo)

        maior = max(maiores)
        index = maiores.index(maior)
        return lista_Pronta[index]

    def investir(self):
        self.saldoAplicado += self.saldo - 3
        self.saldo = 0
        self.posi = 0







