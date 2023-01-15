from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for pessoa in range (1,8):

    nascimento = int(input('Qual o ano de nascimento da {}ª pessoa?: '.format(pessoa)))
    idade = atual - nascimento

    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} maiores de idade e {} menores de idade'.format(totmaior,totmenor))
