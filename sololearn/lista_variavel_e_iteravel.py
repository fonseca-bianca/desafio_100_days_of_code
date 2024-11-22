"""
List Comprehension:
tags é variável porque armazena a lista e também é iterável porque pode ser 
percorrida elemento por elemento no list comprehension.
"""

tags = ["travel", "vacation", "journey"]
hashtags = ["#" + x for x in tags]
print(hashtags)


"""
Criar uma lista com strings em MAIÚSCULAS utilizando método capitalize():
"""

cities = ["Vancouver", "Estocolmo", "Oslo"]
cities = [city. capitalize() for city in cities]
print(cities)