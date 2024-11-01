"""
Faça uma função que mostre que as luzes estão acesas se o argumento for True
"""

lights_on = True
lights_off = False

def show_lights_on(is_on):
    if is_on == True:
        print("As luzes estão acesas!")
    else:
        print("As luzes estão apagadas.")
        
show_lights_on(lights_on)
show_lights_on(lights_off)