"""
CONJUNTOS/SETS:
Ao contrário das Listas e das Tuplas, são coleções desordenadas criadas com {}.
NÃO suportam indexação ou fatiamento.
NÃO podem ter duplicatas. Garante que cada item na coleção será único.
OBS.: itens duplicados NÃO causam erros, mas são IGNORADOS
Assim como listas e tuplas, podem ter valores de diferentes tipos de dados.
estrutura de dados que armazena elementos únicos e não mantém uma ordem 
específica. Quando você imprime um conjunto, Python pode exibir os elementos 
em uma ordem diferente da ordem de inserção.
"""

guests = {"Mery", "Anna", "Jonathan"}
print(guests)
# print(guests[1]) --> NÃO suporta indexação ou fatiamento.

print()
friends = {"Anna", "Anna", "Josh"}
print(friends) # output: {'Anna', 'Josh'}

print()
car_technical_sheet = {"Hyndai", "i30", 2009, 2.0}
print(car_technical_sheet) # output: