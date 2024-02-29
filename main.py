menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
numero_saques, saldo_atual, saldo, total_saques = 0, 0, 0, 0
transacoes = {"depositos": {}, "saques": {}}
limite = 500
extrato = ""
LIMITE_SAQUES = 3
numero_transacoes = 1

while True:
    opcao = input(menu)

    if opcao == "d":
       deposito = int(input("Informe o valor que deseja depositar: "))
       saldo_atual += deposito
       transacoes["depositos"][numero_transacoes] = deposito
       numero_transacoes += 1

       if deposito < 0:
           print("Insira um valor válido para depósito!")

       else:
           continue

    elif opcao == "s":

        while numero_saques != LIMITE_SAQUES:
            saque = int(input("Informe o valor que deseja sacar: "))

            if saque > 0 and saque <= 500:
                print(f"Saque de R$ {saque:.2f} realizado. Saldo atual de: R$ {saldo_atual - saque:.2f}")
                saldo_atual -= saque
                transacoes["saques"][numero_transacoes] = saque
                numero_transacoes += 1
                numero_saques += 1

            elif saldo_atual <= 0:
                print("Não é possível realizar a operação. Saldo insuficiente.")

            else:
                print("Para saques, são permitidos valores positivos e de no máximo R$ 500.00 por operação")



    elif opcao == "e":
        for numero_transacoes, deposito in transacoes["depositos"].items():
            print(f"{numero_transacoes}º Depósito: R$ {deposito:.2f}")

        for numero_transacoes, saque in transacoes["saques"].items():
            print(f"{numero_transacoes}º Saque: R$ {saque:.2f}")


        print(f" Saldo remanescente: R$ {saldo_atual:.2f}")


    elif opcao == "q":
        print("Muito obrigado por utilizar os nossos serviços! Até logo!")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada")
