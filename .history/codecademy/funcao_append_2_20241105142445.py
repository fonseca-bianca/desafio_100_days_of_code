"""
Defina uma função que recebe a playlist e uma música como argumentos e 
adc a música à playlist.
"""
music = input("Adicione uma música que você gosta: ")
playlist = []

def add_menu(playlist, music):
    playlist.append(music)

add_menu()
print(add_menu(playlist))