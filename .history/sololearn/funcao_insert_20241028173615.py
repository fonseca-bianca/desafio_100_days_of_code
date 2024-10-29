"""
Função .insert():
permite adcionar elemento a uma lista em uma posição específica.
Recebe 2 argumentos: 1º é o índice onde será inserido, 2º é o que deverá ser inserido.
"""

items = ["book", "pen", "eraser"]
items.insert(3, "pencil")
print(items)
print(items[3])

print()
colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
print(colors)

print()
colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])

# Após as operações, a lista colors ficará assim:
# ["Red", "Blue", "Green", "Yellow", "Black"]