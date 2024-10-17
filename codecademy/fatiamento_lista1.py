"""
Fatiamento em Python:
a notação de fatiamento com o índice do primeiro item que deseja (inclusivo) e 
o índice final (exclusivo), que deve ser um além do último índice real da lista.
ex.: 
myList = [0,1,2,3,4]
myList[3:5] --> 4 + 1 = :5
# Returns [3, 4]
"""

"""
1.
Na linha 23, crie uma lista chamada middlecontendo apenas os dois itens do meio 
de suitcase.
Na linha 26, crie uma lista chamada lastcomposta apenas pelos dois últimos itens 
de suitcase.
"""

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items 
first = suitcase[0:2]

# Third and fourth items 
middle = suitcase[2:3]

# The last two items 
last =  suitcase[4:5]