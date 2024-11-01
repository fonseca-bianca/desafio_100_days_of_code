"""
Faça uma função que mostre que as luzes estão acesas se o argumento for True
"""

def show_lights_on(is_on):
    if is_on == True:
        print("As luzes estão acesas!")
    else:
        print("As luzes estão apagadas.")
        
show_lights_on(True)


print()
# se declarar a variável ANTES, então o cód ficaria:

lights_on2 = True

def show_lights_on2(is_on2):
    if is_on2:
        print("As luzes estão acesas!")
    else:
        print("As luzes estão apagadas.")
        
show_lights_on2(lights_on2)