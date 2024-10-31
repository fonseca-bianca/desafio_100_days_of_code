"""
A reutilização é uma grande vantagem das funções. A função add_menu do 
exemplo anterior pode ajudar a criar um novo menu do zero. Para fazer isso, 
primeiro você precisa criar uma lista vazia.
"""

new_menu = []

dish1 = 'Pasta'
dish2 = 'Pizza'
dish3 = 'Salad'

def add_to_menu(menu, dish):
    menu.append(dish)
    
add_to_menu(new_menu, dish1)
print(new_menu)


add_to_menu(new_menu, dish2)
print(new_menu)

add_to_menu(new_menu, dish3)
print(new_menu)
