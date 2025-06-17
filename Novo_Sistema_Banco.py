# menu principal
def menu():
    menu_texto = '''
========== MENU ==========
[1] - Depositar
[2] - Sacar 
[3] - Nova Conta 
[4] - Listar Conta 
[5] - Novo Usuário
[6] - EXtrato
[7] - Sair
=> '''
    return input(menu_texto)

# essa função ve se ja tem um usuario existente e se caso não ele não exista ela cria um 
def criar_usuario(usuarios):
    cpf = str(input("Digite seu CPF por favor, apenas os numero:")).strip()

    for usuario in usuarios : 
        if usuario["cpf"] == cpf:
            print("já tem um usuario com esse CPF.")
        return
    
    nome = input("Digite o nome completo?:").title().strip()
    for palavra in ["da", "dos", "do", "e", "di", "a", "de"]:
        nome = nome.replace(palavra.title(), palavra)
    data_nascimento = input("Digite sua data de nascimento(dd/mm/aaaa):")
    endereço = input("Informe seu endereço(lagradouro, n° - bairro - cidade/UF):")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereço
    })
    print("usuario criado com sucesso!")

# essa função cria uma conta 
def criar_conta(agencia, numero_conta, usuario):
    cpf = input("informe seu cpf para validar sua conta:").strip()
    usuario = next((usuario for usuario in usuario if usuario["cpf"] == cpf), None)

    if usuario:
        print("Conta cria com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("Usuario não encontrado.")
        return None
    
# essa função e responsavel pelo deposito
def depositar(saldo,  valor, extrato, /):
    if valor > 0:
        saldo+= valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Depósito realizdo!")
    else:
        ("Valor invalido")
    return saldo, valor

# essa função e responsavel pelo saque 
def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    if valor > saldo:
        print("saldo insulficiente.")
    elif valor > limite: 
        print("o valor que você quer sacar e maior do que seu limite")
    elif numero_saque >= limite_saque:
        print("Número maxímo de saque atingido")
    elif valor > 0:
        saldo -= valor
        extrato += f"saque : R${valor:.2f}\n"
        numero_saque += 1 
        print("Saque realizado!")
    else: 
        print("valor invalido")
    return saldo, extrato, numero_saque

# essa funçaõ exibe o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(50, "="))
    print(extrato if extrato else "não foram relizadas movimentações.")
    print(f"saldo: R${saldo:.2f}")
    print("===============================")

# essa funçao lista todas as contas criadas 
def listar_contas(contas):
    for conta in contas:
        print(f'''
agencia: {conta["agencia"]}
conta: {conta["numero_conta"]}
titular: {conta["usuario"]["nome"]}
''')

# esse e o programa principal
def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    LIMITE_SAQUES = 3 
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float("informe o valor do depósito:")
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("informe o valo do saque"))
            saldo, extrato, numero_saque = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUES, 
            )

        elif opcao == "3":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "4":
            listar_contas(contas)

        elif opcao == "5":
            criar_usuario(usuarios)
        
        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "0":
            print("peograma encerrado")
            break

        else:
            print("Operação inválida. Tente novamente")
            
if __name__ == "__main__":
    main()