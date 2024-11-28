import sys
sys.path.append(r"C:\Users\henri\OneDrive\Documentos\CursoEmVideo\Mundo 3")

from exer112.utilidadescev import dado
from exer112.utilidadescev import moeda


p = dado.leiaDinheiro('Digite o preço:R$')
moeda.resumo(p, 35, 22)
