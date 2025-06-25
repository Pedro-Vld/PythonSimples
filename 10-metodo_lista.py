filmList = ['Duna', 'Jogos Vorazes', 'Senhor dos Aneis', 'Vingadores']

#1-Tamanho da lista
print(len(filmList))

#2- Recuperar um item da lista pelo índice
print(filmList.index('Vingadores'))

#3- Adicionar item  no final da lista
filmList.append('Interstellar')
print(filmList)

#4- Ordenar a lista
filmList.sort()
print(filmList)

#5- Copiar os itens de uma lista para outra
filmCopy = filmList.copy()
filmCopy.remove('Vingadores')
print(filmCopy)

#6- Remove todos os itens da lista
filmList.clear()
print(filmList)