"""
A função pop() remove o item com o nome de chave especificado. 
Ela aceita a chave do item que você deseja remover como argumento.
"""

car = {
    "Brand": "Ford",
    "Model": "Ecosport",
    "Color": "Black"
}

car.pop("Color")
print(car)