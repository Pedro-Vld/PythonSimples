filmDuna ={
    'title': 'Duna',
    'yearRelease': 2021,
    'imdbRating': 8.8,
    'genre': ['sci-fi', 'Action', 'Adventure']

}
print(filmDuna)
print(len(filmDuna))
print(type(filmDuna))

#1- Recuperar um elemento do dicionário
print(filmDuna['genre'])
print(filmDuna.get('imdbRating'))

#2- Buscar apenas as chaves do dicionário
print(filmDuna.keys())

#3- Buscar apenas os valores do dicionário
print(filmDuna.values())

#4- Buscar itens do dicionário com chave e valor
print(filmDuna.items())

#5- Adcionar itens no dicionário
filmDuna['director'] = 'Denis Villeneuve'
print(filmDuna)

#6- Atualizar itens no dicionário
filmDuna.update({'imdbRating': 9.0})
print(filmDuna)

#7- Remover um item no dicionário
filmDuna.pop('director')
print(filmDuna)