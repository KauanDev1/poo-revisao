class Churras:
    def __init__(self, convidados):
        self.convidados = convidados
        self.preco = 82.40

    def mostrarCusto(self):
        kilos = self.convidados * 0.4
        custo = kilos * self.preco
        print(f"o custo pra festa com {self.convidados} pessoas é de {custo:.2f} reais")

quantidade = int(input("quantidade de pessoas na sua festa "))
festa = Churras(quantidade)
festa.mostrarCusto()





    