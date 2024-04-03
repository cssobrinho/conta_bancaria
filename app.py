#coding: utf-8

import textwrap

def menu():
    menu = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar 
    [e]\tExtrato
    [u]\tNovo Usuário
    [n]\tNova Conta
    [l]\tListar Constas
    [q]\tSair 
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informatdo é inválido. @@@")
    
    return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):
    
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques > limiteSaques

    if excedeuSaldo:
        print("\n@@@ Operação falhou!Saldo insuficiente. @@@")

    elif excedeuLimite:
         print("\n@@@ Operação falhou! Limite excedido. @@@")

    elif excedeuSaques:
         print("\n@@@ Operação falhou! Númeo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeroSaques += 1
        print("\n=== Saque efetuado com sucesso. ===")
            
    else:
         print("\n@@@ Operação falhou! O valor informatdo é inválido. @@@")

    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR& {saldo:.2f}")
    print("==================================================")

def criarUsuario(usuarios):
    cpf = input("Digite o número do cpf (só números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Esse usuário já existe com esse CPF. @@@")
        return
    
    nome = input("Digite o nome e sobrenome: ")
    dataNascimento = input("Digite a data de nascimento (nesse formato dd-mm-aaa): ")
    endereco = input("Digite o endereço (nesse formato: rua, n°, bairro, cidade - estado): ")

    usuarios.append({"nome": nome, "data-de-nascimento": dataNascimento, "cpf": cpf, "endereço": endereco})

    print("\n=== Criado novo usuário com sucesso! ===")

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(AGENCIA, numeroConta, usuarios):
    cpf = input("Digite o número do cpf (só números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso. ===")
        return {"agencia": AGENCIA, "numero-da-conta": numeroConta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, criação de conta finalizada. @@@")

def listarContas(contas):

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero-da-conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
               valor = float(input("Digite o valor do saque: "))
               
               saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numeroSaques=numeroSaques,
                    limiteSaques=LIMITE_SAQUES,
               )

        elif opcao == "e":
            exibirExtrato(saldo, extrato=extrato)

        elif opcao == "u":
            criarUsuario(usuarios)

        elif opcao == "n":
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA, numeroConta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listarContas(contas)

        elif opcao == "q":
            break


main()







