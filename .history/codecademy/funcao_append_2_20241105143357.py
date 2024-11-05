"""
Defina uma função que recebe a playlist e uma música como argumentos e 
adc a música à playlist.
"""
playlist = []

def add_menu(playlist, music):
    playlist.append(music)

while True:
    music = input("Adicione uma música que você gosta (ou digite 'sair' para terminar): ")
    if music.lower() == 's':
        break
    add_menu(playlist, music)

print("Suas músicas na playlist são: ")
print(playlist)
