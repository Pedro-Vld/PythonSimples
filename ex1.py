# 1- Escreva um programa que leia dois nomes e retorne uma string formatada no formato "ÚltimoNome, PrimeiroNome".

# 2- Inverta a ordem das palavras em uma string fornecida.

# 3- Verifique se uma string fornecida é um palíndromo _ (pode ser lida da mesmoa forma de trás para frente).

### 1

primeiroNome = input('Digite o seu primeiro nome:\n')
ultimoNome = input('Digite seu sobrenome:\n')

print(f'{ultimoNome}, {primeiroNome}')

### 2

# string = 'estou aprendendo python'
# print(string[::-1])
# jeito que eu fiz

# CORREÇÃO

string = "Estou aprendendo python"
palavras = string.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

### 3 

txt = input('Digite uma palavra para verificar se é um palíndromo:\n')
txt.lower().replace(' ', '')

palindromo = txt == txt[::-1]

print(palindromo)
