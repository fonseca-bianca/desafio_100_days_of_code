"""
CONJUNTOS/SETS:
como são mutáveis, aceitam funções como add() e remove().
OBS.: função append() NÃO funciona com SET, somente com coleções ORDENADAS 
(listas) e adc item ao final da lista.
"""

names_of_people = {"Jim", "Joshua", "Jeremy"}
names_of_people.add("Marrie")
names_of_people.remove("Jim")
print(names_of_people)

print()
students = {"Annabel", "Mathew", "Scott"}
students.clear()
students.add("Sammy")
print(students)