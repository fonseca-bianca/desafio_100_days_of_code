"""
DICIONÁRIOS:
Listas NÃO podem servir como {chaves}, pois, diferentemente da string, NÃO são
Imutáveis.
Strings, inteiros, e tuplas (desde que as tuplas contenham apenas elementos 
Imutáveis) são exemplos de tipos que podem ser usados como chaves em 
dicionários.
Podem ter valores duplicados, mas {chaves} duplicadas NÃO.
OBS.: {chaves} duplicadas SOBRESCREVEM valores já existentes.
Valores: são acessados usando as próprias keys.
"""

car = {
    "brand": "Kia",
    "model": "Sorento",
    "model": "Sportage" # vai SOBRESCREVER o valor anterior dessa {chave}
}
print(car)
# output: {'brand': 'Kia', 'model': 'Sportage'}

print()
# Acessando valores usando as próprias keys (NÃO os índices)
car_2 = {
    "brand": "Ford",
    "model": "EcoSport",
    "year": "2008" 
}
print(car_2["brand"])
print(car_2["model"])
print(car_2["year"])
# output:
# Ford
# EcoSport
# 2008