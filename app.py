import os

restaurantes = [
    {
        'nome': 'Praça',
        'categoria': 'Japonesa',
        'ativo': False
    },
    {
        'nome': 'Pizza Suprema',
        'categoria': 'Pizza',
        'ativo': True
    },
    {
        'nome': 'Cantina',
        'categoria': 'Massa',
        'ativo': False
    },
]

def exibir_nome_do_programa():
    print(""" 
        SABOR EXPRESS
    """)

def exibir_opcoes():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Alternar estado do restaurante')
    print('4- Sair')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():

    ''' 
    Essa função é responsável por cadastrar um novo restaurante 

    inputs: 
    -Nome do restaurante
    -Categoria

    Output:
    -Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novo restaurante')
    nome_do_restaurante = str(input('Digite o nome do restaurante que deseja cadastrar: '))
    categoria = str(input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: '))
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': True
    }
    restaurantes.append(dados_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} criado com sucesso!!')
    voltar_ao_menu_principal()

def listar_restaurantes():

    ''' Essa função é responsável por listar todos os restaurante cadastrados no app '''

    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- nome: { nome_restaurante.ljust(20) } | categoria: { categoria.ljust(20) } | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():

    ''' 
    Essa função é responsável por alternar o estado do restaurante pelo o nome 
    
    inputs: 
    -Nome do restaurante

    Output:
    -Alterna o estado "ativo" do restaurante (Treu ou False)

    '''

    exibir_subtitulo('Alternando estado do restaurante\n')

    nome_restaurante = str(input('Digite o nome do restaurante que deseja alternar o estado: '))

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    voltar_ao_menu_principal()


def finalizar_app():

    ''' Essa função é responsável por fechar o app '''

    exibir_subtitulo('Finalizando App')

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print(f'Você escolheu a opção: {opcao_escolhida }')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()