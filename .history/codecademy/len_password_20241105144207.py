"""
Defina uma gunção pra retornar True se o comprimento da senha for maior ou igual 
a 8.
"""
from Demos.security.sspi.validate_password import password

def verify_length(verify_password):
    if len(verify_password) >= 8:
        return True
    
verify_length()
print(password)