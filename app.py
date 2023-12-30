#coding: utf-8

menu = """

[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 

=> """

deposito = 0
saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do deposito: "))
        
        if  valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Valor inválido, digite um valor valido, por favor.\n")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        
        if  (valor <= limite) and (valor>0) and (numeroSaques < LIMITE_SAQUES):
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numeroSaques += 1             
        elif valor > saldo:
            print("Valor de saque maior do que o valor de saldo.")
        elif numeroSaques >= LIMITE_SAQUES:
            print("Número de saques excedidos para hoje.")
        elif valor > limite:
            print("Valor de saque maior do que o valor de saque diario.")
        else:
            print("Valor inválido, digite um valor valido, por favor.\n")


    elif opcao == "e":
        print("Extrato:\n" + extrato)
        

    elif opcao == "q":
        break

    else:
        print("Opcao inválida, por favor selecione novamente a operação desejada.")
