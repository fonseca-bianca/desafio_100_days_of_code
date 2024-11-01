"""
O operador 'in' permite verificar facilmente se um item está numa lista 
específica.
Ele retorna True se o item ocorrer uma ou mais vezes na lista, e False se não 
ocorrer.
"""

book_list = ['Silmarillion', 'Foundation', "Harry Potter and the philosopher's stone"]
book_name = 'Clean Code'

def book_in_library(book_list, book_name):
    return book_name in book_list

print(book_in_library(book_list, book_name))

# Output: False pq 'Clean Code' NÃO está na lista de livros