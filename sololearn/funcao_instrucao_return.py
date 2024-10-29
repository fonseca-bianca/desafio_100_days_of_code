"""
O resultado de uma função pode ser enviado de volta com a instrução 'return'. 
Isso é particularmente útil quando você precisa continuar usando o valor do 
resultado em seu programa.
"""

def imc(weight, height):
    index = weight / (height * height)
    return index # envia o valor de retorno de volta

# chamando a função 'imc' e usando o valor do 'return'
patient_1 = imc(61, 1.83) # armazena valor de retorno
print(f"Underweight Patient_1: {patient_1:.2f}", patient_1 < 18.5)

# chamando a função 'imc' e usando o valor do 'return'
patient_2 = imc(75, 1.50) # armazena valor de retorno
print(f"Underweight Patient_2: {patient_2:.2f}", patient_2 < 18.5)
