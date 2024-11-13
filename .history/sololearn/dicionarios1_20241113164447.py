"""
DICIONÁRIOS: 
Utilize {chaves}
Tipos de coleções usados pra armazenar dados (itens)
em pares chave:valor. 
Ideais pra organizar dados em pares. Cada dado (valor) tem um identificador (chave)
único na memória.
Chave: valor pares são separados por vírgula e escritos cada um em uma linha =
legibilidade.
Funções values() e keys(): forma de obter TODOS os valores de {chaves} do dicio.
Função items(): retorna TODOS ospares de chave:valor do dicio.
"""

product = {
    "name": "watch",
    "color": "black",
    "brand": "Samsung",
    "model": "Galaxy Smart Watch 6"
}
print(product)

print()
car = {
    "brand": "Audi",
    "model": "Q5"
}
# CHAVES: "brand", "model"
# VALORES: "Audi", "Q5"

print()
# Funções values() e keys()

contact = {
    "name": "Robert",
    "company": "Microsoft"
}

info_keys = contact.keys()
info_values = contact.values()

print(info_keys)
print(info_values)

print()
# Função items():

car_items = {
    "brand": "Ford",
    "color": "silver"
}

info_car = car_items.items()
print(info_car)