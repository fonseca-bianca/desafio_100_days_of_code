"""
1 .
Escreva um for-loop que itere sobre start_liste .append()s cada número ao 
quadrado ( x ** 2) para square_list.
Então classifique square_list!
"""

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
square_list.sort() # sort(): organiza a lista em ordem crescente

print(square_list)

# Quando number é 5, 5 ** 2 = 25, então square_list = [25 --> append: adc ao final].
# Quando number é 3, 3 ** 2 = 9, então square_list = [25, 9 --> append: adc ao final].
# Quando number é 1, 1 ** 2 = 1, então square_list = [25, 9, 1 --> append: adc ao final].
# Quando number é 2, 2 ** 2 = 4, então square_list = [25, 9, 1, 4 --> append: adc ao final].
# Quando number é 4, 4 ** 2 = 16, então square_list = [25, 9, 1, 4, 16 --> append: adc ao final].