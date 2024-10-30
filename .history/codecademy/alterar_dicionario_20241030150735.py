"""
Dicionários podem ser alterados e ter itens removidos com o del
ex.: del dicionario_ja_existente[nome_chave] --> vai remover nome_chave e o respectivo valor dela

NOVO valor:
atribuir um novo valor para a chave
ex.: dicionario_ja_existente[nome_chave] = novo_valor

1.Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.
Set the value associated with 'Rockhopper Penguin' to anything other than 
'Arctic Exhibit'.
"""

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
"""
Poderia excluir ambos em um comando só usando um loop for:
for animal in ['Sloth', 'Bengal Tiger']:
    del zoo_animals[animal]

CASO CONTRÁRIO, dá erro tentar excluir ambas as chaves, pq NÃO são uma Tupla (('Sloth', 'Bengal Tiger'))
"""


zoo_animals['Rockhopper Penguin'] = 'Antartida'

print(zoo_animals)