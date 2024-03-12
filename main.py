def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    while numero_saques != limite_saques:
        saque = int(input("Informe o valor que deseja sacar: "))

        if saque > 0 and saque <= limite:
            print(f"Saque de R$ {saque:.2f} realizado. Saldo atual de: R$ {saldo - saque:.2f}")
            saldo -= saque
            extrato.append(("saque", saque))
            numero_saques += 1

        elif saldo <= 0:
            print("Não é possível realizar a operação. Saldo insuficiente.")

        else:
            print(f"Para saques, são permitidos valores positivos e de no máximo R$ {limite:.2f} por operação")

    return saldo, extrato


def deposito(saldo, valor, extrato):
    deposito_valor = int(input("Informe o valor que deseja depositar: "))
    saldo += deposito_valor
    extrato.append(("deposito", deposito_valor))
    print(f"Depósito de R$ {deposito_valor} efetuado!")

    escolha = input("Deseja fazer outro depósito? S/N ")

    if escolha.lower() == 's':
        return deposito(saldo, valor, extrato)
    else:
        return saldo, extrato


def extrato(saldo, *, extrato):
    for tipo, valor in extrato:
        print(f"{tipo.capitalize()}: R$ {valor:.2f}")

    print(f"Saldo remanescente: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla Estado): ")

    # Verifica se o CPF já existe na lista de usuários
    cpf_existente = any(user['cpf'] == cpf for user in usuarios)

    if cpf_existente:
        print("Erro: CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
        return None

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

    return usuario


def criar_conta_corrente(usuarios, contas):
    cpf = input("Informe o CPF do usuário para vincular à conta corrente: ")

    # Filtra a lista de usuários em busca do CPF informado
    usuario_encontrado = next((user for user in usuarios if user['cpf'] == cpf), None)

    if not usuario_encontrado:
        print("Erro: Usuário não encontrado. Certifique-se de que o CPF está correto.")
        return None

    # Cria uma nova conta corrente
    conta = {
        'agencia': '0001',
        'numero_conta': len(contas) + 1,
        'usuario': usuario_encontrado
    }

    contas.append(conta)
    print(f"Conta corrente criada com sucesso! Número da conta: {conta['numero_conta']}")

    return conta


def exibir_usuarios_e_contas(usuarios, contas):
    print("\nLista de usuários cadastrados:")
    for usuario in usuarios:
        print(usuario)

    print("\nLista de contas correntes cadastradas:")
    for conta in contas:
        print(conta)


def menu():
    usuarios_cadastrados = []
    contas_cadastradas = []

    saldo_atual = 0
    extrato_atual = []
    limite_saque = 500
    numero_saques_atual = 0
    limite_saques = 3

    while True:
        opcao = input("""
    Escolha uma das opções abaixo:
    [1] Criar Usuário
    [2] Criar Conta Corrente
    [3] Saque
    [4] Depósito
    [5] Extrato
    [6] Exibir Usuários e Contas
    [q] Sair

    """)

        if opcao == "1":
            criar_usuario(usuarios_cadastrados)

        elif opcao == "2":
            criar_conta_corrente(usuarios_cadastrados, contas_cadastradas)

        elif opcao == "3":
            saque_resultado = saque(saldo=saldo_atual, valor=0, extrato=extrato_atual,
                                    limite=limite_saque, numero_saques=numero_saques_atual, limite_saques=limite_saques)
            saldo_atual, extrato_atual = saque_resultado

        elif opcao == "4":
            deposito_resultado = deposito(saldo=saldo_atual, valor=0, extrato=extrato_atual)
            saldo_atual, extrato_atual = deposito_resultado

        elif opcao == "5":
            extrato(saldo=saldo_atual, extrato=extrato_atual)

        elif opcao == "6":
            exibir_usuarios_e_contas(usuarios_cadastrados, contas_cadastradas)

        elif opcao.lower() == "q":
            print("Muito obrigado por utilizar os nossos serviços! Até logo!")
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada")


# Chama a função menu para iniciar o programa
menu()
