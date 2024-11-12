"""
CONJUNTOS/SETS:
como são mutáveis, aceitam funções como add() e remove().
OBS.: função append() NÃO funciona com SET, somente com coleções ORDENADAS 
(listas) e adc item ao final da lista.
Função clear() NÃO aceita argumentos e remove TODOS os itens de um SET.
Função union() retorna um NOVO SET com TODOS os elementos de AMBOS os SETS,
omitindo os itens duplicados. É chamada em um SET e aceita OUTRO SET como argumento
Função difference() retorna SET com elementos q estão APENAS no primeiro SET (e 
NÃO no segundo SET)
"""

names_of_people = {"Jim", "Joshua", "Jeremy"}
names_of_people.add("Marrie")
names_of_people.remove("Jim")
print(names_of_people)

print()
# Função clear() NÃO aceita argumentos e remove TODOS os itens de um SET.
students = {"Annabel", "Mathew", "Scott"}
students.clear() # vai remover TODOS os itens
students.add("Sammy")
print(students)

print()
""" Função union() retorna um NOVO SET com TODOS os elementos de AMBOS os SETS,
omitindo os itens duplicados.
É chamada em um SET e aceita OUTRO SET como argumento """
s_set1 = {"apple", "banana"}
s_set2 = {"banana", "strawberry"}
s_sets_combined = s_set1.union(s_set2)
print(s_sets_combined) # output: a cada impressão será um resultado, porém, 'banana', NÃO se repetirá


print()
""" Função difference() retorna SET com elementos q estão APENAS no primeiro SET (e 
NÃO no segundo SET) """

s_set_A = {"apple", "banana", "cherry"}
s_set_B = {"banana", "cherry", "grape"}
s_set_difference = s_set_A.difference(s_set_B)
print(s_set_difference) # output: {'apple'}
# "apple" é o único elemento exclusivo de s_set_A que não aparece em s_set_B.