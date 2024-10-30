"""
Python permite que os argumentos da função tenham valores padrão. 
Se a função é chamada sem o argumento, o argumento recebe seu valor padrão.
Valor padrão: usado SOMENTE se NENHUM outro valor foi passado como argumento pra função chamada.
"""


def greet(name = "Michael"):
    print("Welcome", name)
    
greet() # aqui vai chamar o valor padrão
greet("John Oliver") # aqui vai chamar o valor passado no argumento da função

# Welcome Michael
# Welcome John Oliver