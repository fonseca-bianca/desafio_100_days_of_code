"""
Você pode usar o OPERADOR 'in' para verificar se uma chave ou um valor 
existe em um dicionário.
"""

zoo_animals = {
    'Lion': 'Africa',
    'Elephant': 'Africa',
    'Sloth': 'Africa'
}
print("Color" in zoo_animals) # output: False

"""
Para verificar se um valor ocorre em um dicionário, você precisa usar a 
FUNÇÃO 'values()'.
"""

print(zoo_animals.values())