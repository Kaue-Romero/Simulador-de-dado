from random import randint

n1 = int(input('Quantos lados o dado tem ? '))
n2 = randint(1, n1)

while True:
    n = str(input('Você que jogar o dado? ')).upper().strip()
    while n not in 'SN':
        n = str(input('Você que jogar o dado? [S/N] ')).upper().strip()
    if n == 'S':
        n2 = randint(1, n1)
        print(f'Você jogou o dado e caiu em {n2}')
        n1 = int(input('Quantos lados o dado tem ? '))
    else:
        break
print('Obrigado por usar o código')
