def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor

#Programa principal
n= leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')