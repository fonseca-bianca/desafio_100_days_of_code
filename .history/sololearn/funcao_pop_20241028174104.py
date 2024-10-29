"""
Função .pop():
remove um elemento da lista.
Único argumento é o índice da posição que se deseja remover da lista.
"""

items = ["book", "pen", "eraser"]
items.pop(1)
print(items)
print(items[1]) # passa a ser "eraser"


""" Remova o 3º elemento e depois adicione 95 ao final da lista"""
points = [15, 36, 74, 88]
points.pop(2)
points.append(95, [4])
print(points)