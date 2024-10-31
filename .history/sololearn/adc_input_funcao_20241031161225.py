"""
Você pode obter entradas do usuário ao chamar uma função.
Este código solicita uma entrada do usuário cada vez que a função é chamada, 
adicionando o valor inserido à lista:
"""

cart = []

def add_to_cart(cart):
    product = input("Insira aqui um valor: ")
    cart.append(product)
    
add_to_cart(cart)
print(cart)