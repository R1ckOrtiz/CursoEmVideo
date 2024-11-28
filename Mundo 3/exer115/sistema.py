import sys
sys.path.append(r"C:\Users\henri\OneDrive\Documentos\CursoEmVideo\Mundo 3")

from exer115.lib.interface import *
from exer115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
      resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
      if resposta == 1:
         # Opção de listar o conteúdo de um arquivo!
         lerArquivo(arq)
      elif resposta == 2:
          cabeçalho('NOVO CADASTRO')
          nome = str(input('Nome:'))
          idade = leiaInt('Idade:')
          cadastrar(arq, nome, idade)
      elif resposta == 3:
          cabeçalho('Saindo do sistema... Até logo!')
          break
      else:
          print('\033[31mERRO! Digite uma opção válida!\033[m')
      sleep(2)


