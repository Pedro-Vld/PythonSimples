import pprint

filmsDict = {
    'Duna': {
        'title': 'Duna',
        'yearRelease': 2021,
        'imdbRating': 8.8,
        'genre': ['sci-fi', 'action', 'adventure']
    },
    'Jogos Vorazes': {
        'title': 'Jogos Vorazes',
        'yearRelease': 2012,
        'imdbRating': 7.5,
        'genre': ['thriller', 'action', 'adventure', 'drama']
    },
    'Senhor dos Aneis':{
        'title': 'Senhor dos Aneis',
        'yearRelease': 1954,
        'imdbRating': 10,
        'genre': ['fantasy', 'action', 'adventure', 'epic']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

#1- Buscar uma informação dentro um dicionário aninhado
print(filmsDict['Duna']['genre'])

#2- Adicionar novo item
filmsDict['Duna']['director'] = 'Denis Villeneuve'
print(filmsDict['Duna'])

#3- Excluir um dicionário
del filmsDict['Jogos Vorazes']
pp.pprint(filmsDict)
