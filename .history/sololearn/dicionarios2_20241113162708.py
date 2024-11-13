"""
DICIONÁRIOS:
Listas NÃO podem servir como {chaves}, pois, diferentemente da string, NÃO são
Imutáveis.
Strings, inteiros, e tuplas (desde que as tuplas contenham apenas elementos 
Imutáveis) são exemplos de tipos que podem ser usados como chaves em 
dicionários.
Podem ter valores duplicados, mas {chaves} duplicadas NÃO.
OBS.: {chaves} duplicadas SOBRESCREVEM valores já existentes.
"""

car = {
    "brand": "Kia",
    "model": "Sorento",
    "model": "Sportage"
}
print(car)