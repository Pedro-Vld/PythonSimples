# Utilizando a concatenação 

name = input('digite o nome do filme: \n')
yearLaunch = int(input('digite o ano de lançamento do filme: \n'))
noteMovie = float(input('digite a nota do filme: \n'))

print('DADOS DO FILME')
print('=-=-=-=-=-=-=-=')

# Alternativa 1
print('Nome do filme:', name)
print('Ano de lançamento:', yearLaunch)
print('Nota do filme:', noteMovie)

# Alternativa 2
print('Nome do Filme:', name, '\nAno de lançamento:', yearLaunch, '\nNota do filme:', noteMovie)

# Alternativa 3
print(f'Nome do filme: {name}\n'
      f'Ano de lançamento: {yearLaunch}\n'
      f'Nota do filme: {noteMovie}\n'
      )