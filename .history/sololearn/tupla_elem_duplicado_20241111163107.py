"""
Tuplas, como listas, podem conter elementos duplicados.
Você pode usar a função count() para calcular o número de ocorrências de um 
item em uma tupla.
"""

scores = (7, 9, 9, 8, 9)
print("# de 7:", scores.count(7)) # count: conta quantas vzs o número especificado aparece na tupla
print("# de 9:", scores.count(9))
print("# de 2:", scores.count(2))

# output: 1 
# output: 3 
# output: 0 

points = (12, 14, 9, 10, 9)
winner = max(points)
print(winner)