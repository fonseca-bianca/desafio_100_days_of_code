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
names_of_players = ["Anne", "Joseph", "Linda", "Peter"]

def sort_names(names_of_players):
    return sorted(names_of_players) 

print(sort_names(names_of_players))




