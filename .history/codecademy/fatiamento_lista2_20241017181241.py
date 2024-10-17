"""
Fatiamento de listas e strings
Cada caractere é um item sequencial começando em zero
"""

# my_list[:2]
    # Grabs the first two items
# my_list[3:] (3 é o índice do 4º item da lista (3 + 1 = 4))
    # Grabs the fourth through last items

"""
1 .
Atribuir a dog uma fatia animals do índice 3 até , mas não incluindo, o índice 6.
Atribuir a frog uma fatia animals do índice 6 até o final da string.
"""
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]