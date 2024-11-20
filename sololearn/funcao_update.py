"""
A função update() atualiza o dicionário com os itens do argumento fornecido.
O argumento deve ser um dicionário com o item que você deseja atualizar.
Essa função aceita vários itens. Se um item for NOVO, ele será adc ao dicionário
existente .
"""

person = {
    "Name": "Aristoteles",
    "Age": 90
}

person.update({"Age": 89, "Country": "Canada"}) 
# aq vai key + value pq o dicionário é o argumento da função update()

print(person["Age"]) # output: 89
print(person.items()) 
# output: dict_items([('Name', 'Aristoteles'), ('Age', 89), ('Country', 'Canada')])