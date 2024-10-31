"""
A reutilização é uma grande vantagem das funções. A função add_menu do 
exemplo anterior pode ajudar a criar um novo menu do zero. Para fazer isso, 
primeiro você precisa criar uma lista vazia.
"""

new_menu = [] # lista vazia criada

# declaração das variáveis e valores correspondentes
dish1 = 'Pasta'
dish2 = 'Pizza'
dish3 = 'Salad'

def add_to_menu(menu, dish):
    menu.append(dish)

# adc prato 1 ao menu  
add_to_menu(new_menu, dish1)
print(new_menu)

# adc prato 2 ao menu
add_to_menu(new_menu, dish2)
print(new_menu)

# adc prato 3 ao menu
add_to_menu(new_menu, dish3)
print(new_menu)
