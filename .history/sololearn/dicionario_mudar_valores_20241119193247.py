"""
Você pode usar chaves não apenas para acessar valores em um dicionário,
mas também para mudar eles.
"""

other_user = {
    "Name": "Mariah",
    "Age": 40
}
other_user["Age"] = 42

print(other_user) 
# output: {'Name': 'Mariah', 'Age': 42} (Mostra todo o dicionário como um único objeto.)

print(other_user.items()) 
# output: dict_items([('Name', 'Mariah'), ('Age', 42)])
# Mostra uma "visualização" dos itens (pares chave-valor) do dicionário, retornando um objeto especial chamado 'dict_items'.