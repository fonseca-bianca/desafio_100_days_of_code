zoo_animals = ["pangolin", "cassowary", "sloth", ]

"""
1 .
A lista zoo_animalstem três itens (confira-os na linha 1). Vá em frente e 
adicione um quarto! Basta digitar o nome do seu animal favorito (como um "string")
na linha 1, depois da vírgula final, mas antes do . de fechamento ].
"""

zoo_animals.append("dog")

if len(zoo_animals) > 3:
    print("The first animal at the zoo is the " + zoo_animals[0])
    print("The second animal at the zoo is the " + zoo_animals[1])
    print("The third animal at the zoo is the " + zoo_animals[2])
    print("The fourth animal at the zoo is the " + zoo_animals[3])