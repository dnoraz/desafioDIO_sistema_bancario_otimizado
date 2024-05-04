menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")
  
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if 0 < valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso.')
            elif valor_saque > saldo:
                print("Saldo insuficiente.")
            else:
                print("Valor de saque excede o limite diário.")
        else:
            print("Limite de saques diários atingido.")
        
    elif opcao == "3":
        if extrato:
            print(extrato + f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")
   
    elif opcao == "4":
        print("Obrigado por utilizar nosso banco, até mais...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")