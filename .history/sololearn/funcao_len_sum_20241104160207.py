"""
Utilizando função len() juntamente com a função sum() é possível encontrar
um valor médio
"""

prices = [33, 49, 55, 14]
total = sum(prices)
print("Total price is: ", prices)

number_of_products = len(prices)
print("Number of products is: ", number_of_products)

# cálculo média
average_price = total/number_of_products
print("Average price is: ", average_price)