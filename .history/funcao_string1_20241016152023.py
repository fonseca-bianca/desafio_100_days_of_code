"""
.lower() e .upper():
São funções que só podem ser usadas em strings.
Notação de ponto --> .___():
    funciona somente com certos objetos (strings, listas)
"""
print("SmArTpHoNe".lower())
print("SmArTpHoNe".upper())

print()
# Variáveis podem ser usadas em funções.
brand = "ikea"
print(brand.upper())

print()
# capitalize(): converte 1º caractere MAIÚSCULO e demais minúsculos
print("happy birthday".capitalize())

print()
# title(): 1ª letra de cada palavra fica MAIÚSCULA de mais minúsculas
print("happy birthday".title())

print()
# String é imutável, portanto, qualquer modificação em uma variável deverá 
# ser armazenada em uma nova variável
item_1 = "smartwatch"
print(item_1.upper())
print(item_1)

item_2 = item_1.upper()
print(item_2)