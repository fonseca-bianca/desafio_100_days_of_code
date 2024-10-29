"""
Função personalizada:
1º definir a função pra chamá-la no cód sempre que precisar (cód reutilizável)
"""

def greet(): # nome função
    print("Hello from a function.") # corpo função
    print("Have a nice day!")       # corpo função

greet()
# ao chamar a função sem parâmetros, é ela que faz os comandos print acima serem executados
# por estar SEM Argumentos (NÃO irá receber nenhuma entrada), ela irá executar o bloco de cód q está dentro dela

print()
def say_hello():
    print("Hello, world!")  # apenas imprime uma mensagem

# variável fora da função
message = "This is a message outside the function."

# chamando a função
say_hello()

# imprimindo a variável fora da função
print(message)