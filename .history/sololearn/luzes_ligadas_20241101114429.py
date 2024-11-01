"""
Faça uma função que mostre que as luzes estão acesas se o argumento for True
"""

# lights_on = True
# lights_off = False

# def show_lights_on(is_on):
#     if is_on == True:
#         print("As luzes estão acesas!")
#     else:
#         print("As luzes estão apagadas.")
        
# show_lights_on(True)
# show_lights_on(lights_off)

# se declarar a variável ANTES, então o cód ficaria:

lights_on = True

def show_lights_on(is_on):
    if is_on:
        print("As luzes estão acesas!")
    else:
        print("As luzes estão apagadas.")
        
show_lights_on(lights_on)