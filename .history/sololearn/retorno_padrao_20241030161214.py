"""
Python permite que os argumentos da função tenham valores padrão. 
Se a função é chamada sem o argumento, o argumento recebe seu valor padrão.
Valor padrão: usado SOMENTE se NENHUM outro valor foi passado como argumento pra função chamada.
"""


def greet(name = "Michael"):
    print("Welcome", name)
    
greet()
greet("John Oliver")

# Welcome Michael
# Welcome John Oliver