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

"""No desempacotamento, Python associa cada variável a um elemento da lista na 
sequência:
A primeira variável (winner) recebe o primeiro elemento da lista (98).
O operador * ao lado da variável rest indica que ela deve receber todos os 
elementos restantes na lista, a partir do segundo elemento."""