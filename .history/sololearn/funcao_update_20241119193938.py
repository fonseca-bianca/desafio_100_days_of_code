"""
A função update() atualiza o dicionário com os itens do argumento fornecido.
O argumento deve ser um dicionário com o item que você deseja atualizar.
"""

person = {
    "Name": "Aristoteles",
    "Age": 90
}

person.update({"Age": 89})

print(person["Age"])
print(person.items())