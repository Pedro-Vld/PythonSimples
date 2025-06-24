movieName = 'Top Gun'

movieDescription = '''
    Top Fun Maverick, é um filme de aviação e aventura,
    muito consagrado, na indústria
'''

print(movieName.upper()) # tudo maíusculo 
print(movieName.lower()) # Tudo minúsculo
print(movieName.capitalize()) # Primeira letra da frase maíuscula
print(movieName.title()) # Primeira letra de cada palavra maíuscula
print(movieName.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(movieName.find('u')) # Retorna a posição ou índice de determinado caractere
print(movieName.find('o')) # Conta caracteres
print(movieName.replace('Top', 'Matrix')) # Altera elementos por outros
print(movieDescription.split(',')) # Quebra a string em partes