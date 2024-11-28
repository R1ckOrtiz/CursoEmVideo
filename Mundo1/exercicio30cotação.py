real = float(input('quanto dinheiro você tem na carteira'))
euro = real / 5.56
print('com R${} você pode comprar ¢{:.2f}'.format(real,euro))