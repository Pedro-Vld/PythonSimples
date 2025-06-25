filmsSet = {'Duna', 'Jogos Vorazes', 'Senhor dos Aneis', 'Vingadores'}
print(type(filmsSet))

#1- buscar o tamanho do set
print(len(filmsSet))

#2- True e 1 são considerados o mesmo valor
exempleSet = {'Duna', True, 1, 8.7}
print(exempleSet)

#3- Adcionar item de outro set
filmsSet.update(exempleSet)
print(filmsSet)

#4- Remover um item no set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)
