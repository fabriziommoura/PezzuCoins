# Sistema de moeda virtual: PezzuCoins

# Base de dados (simulada como dicionários e listas)
usuarios = {}
transacoes = []

# Função para cadastrar usuários
def cadastrar_usuario(nickname):
    if nickname in usuarios:
        print(f"Usuário '{nickname}' já existe!")
    else:
        usuarios[nickname] = 2500  # Saldo inicial
        print(f"Usuário '{nickname}' cadastrado com 2500 PezzuCoins.")

# Função para enviar moedas
def enviar_moedas(remetente, destinatario, valor):
    if remetente not in usuarios:
        print(f"Usuário remetente '{remetente}' não encontrado!")
        return
    if destinatario not in usuarios:
        print(f"Usuário destinatário '{destinatario}' não encontrado!")
        return
    if usuarios[remetente] < valor:
        print(f"Saldo insuficiente! {remetente} tem apenas {usuarios[remetente]} PezzuCoins.")
        return
    
    # Atualizar saldos
    usuarios[remetente] -= valor
    usuarios[destinatario] += valor

    # Registrar a transação
    transacoes.append({
        "remetente": remetente,
        "destinatario": destinatario,
        "valor": valor,
    })
    print(f"\n{valor} PezzuCoins enviados de {remetente} para {destinatario}.")
    print(f"Novo saldo de {remetente}: {usuarios[remetente]} PezzuCoins.")
    print(f"Novo saldo de {destinatario}: {usuarios[destinatario]} PezzuCoins.")

# Função para exibir o saldo de um usuário
def exibir_saldo(nickname):
    if nickname in usuarios:
        print(f"Saldo de {nickname}: {usuarios[nickname]} PezzuCoins.")
    else:
        print(f"Usuário '{nickname}' não encontrado!")

# Função para exibir o histórico de transações
def exibir_historico(nickname):
    print(f"\nHistórico de transações para {nickname}:")
    for transacao in transacoes:
        if transacao["remetente"] == nickname or transacao["destinatario"] == nickname:
            print(f"{transacao['remetente']} enviou {transacao['valor']} para {transacao['destinatario']}")

# Menu principal
def menu():
    while True:
        print("\n=== Sistema PezzuCoins ===")
        print("1. Cadastrar usuário")
        print("2. Enviar moedas")
        print("3. Exibir saldo")
        print("4. Exibir histórico de transações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nickname = input("Digite o nickname do usuário: ")
            cadastrar_usuario(nickname)
        elif opcao == "2":
            remetente = input("Digite o nickname do remetente: ")
            destinatario = input("Digite o nickname do destinatário: ")
            valor = int(input("Digite o valor a ser enviado: "))
            enviar_moedas(remetente, destinatario, valor)
        elif opcao == "3":
            nickname = input("Digite o nickname do usuário: ")
            exibir_saldo(nickname)
        elif opcao == "4":
            nickname = input("Digite o nickname do usuário: ")
            exibir_historico(nickname)
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
