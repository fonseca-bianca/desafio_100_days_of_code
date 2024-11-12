"""
CONJUNTOS/SETS:
como são mutáveis, aceitam funções como add() e remove().
OBS.: função append() NÃO funciona com SET, somente com coleções ORDENADAS 
(listas) e adc item ao final da lista.
Função clear() NÃO aceita argumentos e remove TODOS os itens de um SET.
"""

names_of_people = {"Jim", "Joshua", "Jeremy"}
names_of_people.add("Marrie")
names_of_people.remove("Jim")
print(names_of_people)

print()
students = {"Annabel", "Mathew", "Scott"}
students.clear() # vai remover TODOS os itens
students.add("Sammy")
print(students)