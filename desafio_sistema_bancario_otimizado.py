# Definição da função para realizar um saque
def saque(*, saldo, valor, extrato, limite=500, numero_saques=0, limite_saques=3):
    # Verifica se o número de saques diários está dentro do limite
    if numero_saques < limite_saques:
        # Verifica se o valor do saque é válido
        if 0 < valor <= saldo and valor <= limite:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque excede o limite diário.")
    else:
        print("Limite de saques diários atingido.")
    return saldo, extrato

# Definição da função para realizar um depósito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print("Valor de depósito inválido. O valor deve ser positivo.")
    return saldo, extrato

# Definição da função para imprimir o extrato
def imprimir_extrato(saldo, /, *, extrato):
    if extrato:
        print(extrato + f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")

# Lista para armazenar os usuários do banco
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (logradouro, número - bairro - cidade/sigla - estado): ")
    
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário cadastrado com esse CPF.")
            return None
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário cadastrado com sucesso.")
    return usuarios

# Lista para armazenar as contas bancárias
contas = []
# Variável para controlar o número da próxima conta
prox_numero_conta = 1

# Função para cadastrar uma nova conta bancária
def cadastrar_conta_bancaria(agencia, numero_conta, usuarios):
    global prox_numero_conta
    cpf = input("Digite o CPF do titular da conta: ")
    cpf = ''.join(filter(str.isdigit, cpf))
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
            prox_numero_conta += 1
            print("Conta bancária cadastrada com sucesso.")
            return None
    
    print("Não foi encontrado nenhum usuário com o CPF fornecido.")

# Função para listar os usuários e suas contas
def listar_usuarios_contas(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(f"Nome: {usuario['nome']} | CPF: {usuario['cpf']}")
            print("Contas vinculadas:")
            for conta in contas:
                if conta['usuario'] == usuario:
                    print(f"Agência: {conta['agencia']} | Número da conta: {conta['numero_conta']}")
            print("--------------------")
            return
    print("Não foi encontrado nenhum usuário com o CPF fornecido.")

# Menu de operações do banco
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta Bancária
[6] Listar Usuários e Contas
[7] Sair

=> """

# Variáveis iniciais do sistema bancário
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)
  
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        saldo, extrato = saque(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
    elif opcao == "3":
        imprimir_extrato(saldo, extrato=extrato)
    
    elif opcao == "4":
        usuarios = cadastrar_usuario(usuarios)
    
    elif opcao == "5":
        agencia = '0001'  # Agência fixa
        numero_conta = prox_numero_conta
        cadastrar_conta_bancaria(agencia, numero_conta, usuarios)
        
    elif opcao == "6":
        cpf = input("Digite o CPF do usuário para listar suas contas: ")
        listar_usuarios_contas(cpf, usuarios)
   
    elif opcao == "7":
        print("Obrigado por utilizar nosso banco, até mais...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")