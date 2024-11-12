"""
CONJUNTOS:
Ao contrário das Listas e das Tuplas, são coleções desordenadas criadas com {}.
NÃO suportam indexação ou fatiamento.
NÃO podem ter duplicatas. Garante que cada item na coleção será único.
OBS.: itens duplicados NÃO causam erros, mas são IGNORADOS
"""

guests = {"Mery", "Anna", "Jonathan"}
print(guests)
# print(guests[1]) --> NÃO suporta indexação ou fatiamento.

friends = {"Anna", "Anna", "Josh"}
print(friends)