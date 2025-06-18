print('=-='* 20)
print('       MEU ESTOQUE GERAL      ')
print('=-=' * 20)

estoque = []
lista_produto = []

while True:
    comando =  input('Digite um comando: ').strip().lower()

    print('-=='* 10)
    print('     MENU      ')
    print('-='* 10)

    if comando == 'menu':
        print('\n[1] Adicionar produto')
        print('\n[2] verificar produto')
        print('\n[3] Sair')
    try:
        opcao = int(input('Qual opção você deseja :'))
    except ValueError:
        print('Por favor, digite apenas um número valido.')
        continue  # Continua o loop em vez de encerrar

    if opcao == 1:
        nome = input('Nome do produto: ')
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        produto = {'nome': nome, 'quantidade': quantidade, 'preço': preco}
        lista_produto.append(produto)
        print('Produto adicionado com sucesso!\n')
    
    elif opcao == 2:
        if not lista_produto:
            print('Nenhum produto nop estoque!\n')

        else:
            print('Produtos nos estoque: ')
            for i, prod in enumerate(lista_produto, 1):
                total_item = prod['quantidade'] *  prod['preço']
                print(f'{i}. produto: {prod['nome']}')
                print(f'    Quantidade: {prod['quantidade']}')
                print(f'    preço unitario: R$ {prod['preço']}')
                print(f'    Total em estoque R$ {total_item:.2f}\n')
            print()

    elif opcao == 3:
        print('Ate breve!')
        break
    else:
        print('Opção inválida.\n')

    if comando == 'sair':
        print('Encerrando o sistema...')
        break

    else:
        print("Comando desconhecido. Digite 'menu' para ver as opções ou 'sair' para sair.\n")