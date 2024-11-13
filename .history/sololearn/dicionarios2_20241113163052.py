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

print()
# Acessando valores usando as próprias keys (NÃO os índices)
car_2 = {
    "brand": "Ford",
    "model": "EcoSport",
    "year": "2008" 
}
print(car["brand"])
print(car["model"])
print(car["year"])