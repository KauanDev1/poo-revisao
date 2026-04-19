from rich import print
from rich.table import Table
from rich.panel import Panel

tabela = Table()
box = Panel("Preços Mercado do Messi", title="Tabela de preço")

tabela.add_column("ID",)
tabela.add_column("Produto",)
tabela.add_column("Preço")

tabela.add_row("001", "Maçã", "R$20,00", style="red")
tabela.add_row("002", "Pera", "R$15,75", style="green")
tabela.add_row("003", "Uva", "R$9,99", style="purple")

print(box)
print(tabela)