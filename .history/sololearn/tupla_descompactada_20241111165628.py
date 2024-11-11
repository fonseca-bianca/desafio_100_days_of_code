"""
DESEMPACOTAMENTO DE TUPLAS:
O descompacotamento de tuplas permite a atribuição de itens de tuplas a variáveis.
Os valores serão atribuídos na ordem em que aparecem na tupla.
Ao desempacotar, o número de variáveis deve corresponder ao número de itens na 
tupla. Caso contrário, o programa resultará em um erro.
"""

birth_date = (5, "Novembro", 1992) # 3 variáveis = 3 tuplas
day, month, year = birth_date

print(birth_date) # output: (5, 'Novembro', 1992)
print(f"{day} de {month} de {year}") # output: 5 de Novembro de 1992