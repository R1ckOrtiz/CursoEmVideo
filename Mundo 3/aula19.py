estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigal do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.items():
        print(v, end=' ')
    print()