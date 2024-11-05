"""
Defina uma gunção pra retornar True se o comprimento da senha for maior ou igual 
a 8.
"""
verify_password = input("Insira sua senha aqui: ")

def verify_length(verify_password):
    if len(verify_password) >= 8:
        return True
    else:
        return False
    
verify_length(verify_password)
print(verify_length(verify_password))