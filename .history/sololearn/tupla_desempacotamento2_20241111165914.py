"""
DESEMPACOTAMENTO DE TUPLAS:
O operador * no desempacotamento de tuplas é usado para reunir vários elementos
da tupla em uma lista. Isso é útil ao lidar com tuplas de comprimento 
desconhecido.
"""

scores = [98, 99, 100, 101, 102]
winner, *rest = scores
print(winner)
print(rest)