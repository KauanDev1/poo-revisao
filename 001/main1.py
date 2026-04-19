class Pessoa:
    def __init__(self, nome, idade, dinheiro):
        self.nome = str(nome)
        self.idade = int(idade)
        self.dinheiro = int(dinheiro)
        
    def niver(self):
        self.idade += 1
 
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos e tenho {self.dinheiro}..")

    def dinheiroDepositar(self, valor):
        self.dinheiro = self.dinheiro + valor

    def tchau(self):
        print(f"{self.nome}: Adeus")

    
        

kauan = Pessoa("kauan", 18, 10)
kauan.niver()
kauan.niver()
kauan.dinheiroDepositar(100)
kauan.apresentar()

print("====================================")

ana = Pessoa("Ana", 18, 999)
ana.dinheiroDepositar(9999999)
ana.apresentar()




