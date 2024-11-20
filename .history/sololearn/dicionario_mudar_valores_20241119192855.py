"""
Você pode usar chaves não apenas para acessar valores em um dicionário,
mas também para mudar eles.
"""

other_user = {
    "Name": "Mariah",
    "Age": 40
}
other_user["Age"] = 42

print(other_user) # outpu: {'Name': 'Mariah', 'Age': 42}
print(other_user.items()) # output: dict_items([('Name', 'Mariah'), ('Age', 42)])