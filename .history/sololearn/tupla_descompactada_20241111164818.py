"""
A descompactação de tuplas permite a atribuição de itens de tuplas a variáveis.
Os valores serão atribuídos na ordem em que aparecem na tupla.
"""

birth_date = (5, "November", 1992)
day, month, year = birth_date

print(day)
print(month)
print(year)