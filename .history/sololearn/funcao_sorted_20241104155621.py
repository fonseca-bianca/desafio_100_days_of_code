"""
Função sorted(): recebe iterável como entrada.
Retorna uma lista com os itens ordenados.
Lida tanto com valores numéricos quanto textuais.
"""

ages = [10, 12, 5, 59, 89, 99, 9]

def sort_ages(ages):
    return sorted(ages)    

print(sort_ages(ages))
sort_ages(ages)

print()
names_of_players = ["Anne", "Joseph", "Melanie", "Sarah", "Linda", "Peter"]

def sort_names(names_of_players):
    return sorted(names_of_players) 

print(sort_names(names_of_players))

"""
Argumento reverse:
Utilizando o reverse = True, teremos os valores de uma lista classificados em 
ordem descrescente
"""

start_ages = sorted(ages, reverse = True)

print(start_ages)

android = [25, 36, 33, 19, 56]
s_android = sorted(android, reverse = True)
print(s_android[0:3])
