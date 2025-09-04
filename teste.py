nome = input('Digite seu nome: ')
idade = input('digite sua idades: ')

idade_int = int(idade) # Conversão de string para inteiro

if nome and idade_int: # Verificação de valores vazios
    print(f'Seu nome é {nome} ' # f-strings
          f' e você tem {idade_int} anos'
          )
    print(f'Seu nome invertido é {nome[::-1]}') # Inversão de string
    print(f'Seu nome tem {len(nome)} letras') # Contagem de caracteres
    
    print(f'A primeira letra do seu nome é {nome[0]}' # Acesso por índice
          f' e a última é {nome[-1]}' # Acesso por índice negativo
          )
    
    if ' ' in nome: # Verificação de substring
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')


else: # Verificação de valores vazios
    print('Desculpe, você deixou campos vazios')