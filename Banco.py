menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>
"""

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}/n"
        else:
            print("Valor Invalido, por favor insira um valor valido.")
    
    elif opcao == 's':
        valor =  float(input("Informe o valor a ser sacado:"))

        saldo_execedido = valor > saldo
        limite_execedido = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_execedido:
            print("Saldo insuficiente para saque.")
        elif limite_execedido:
            print("Limite de saque excedido.")   
        elif excedeu_saques:
            print("Limite diario excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}/n"
            numero_saques += 1
        else:
            print("O valor informado é invalido, tente novamente!")
    
    elif opcao == 'e':
        texto = "Extrato"
        texto_fim = ""
        print(texto.center(30, "-"))
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(texto_fim.center(30,"-"))
    
    elif opcao == 'q':
        break

    else:
        print("Opção Invalida! Selecione uma opção valida para continuar.")