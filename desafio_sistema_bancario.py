MENU = """ 
############# MENU #############

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

################################
        
""" 

saldo = 0
limite = 500
extrato = ""
total_sacado = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    print(MENU)

    opcao = input("Digite a opção desejada: ").strip()

    # Depositar
        # O limite de depositos é de 500 reais.
        # Se o saldo ultrapassar esse limite, não será possível depositar mais.
    if opcao == '1':
        valor = float(input("\nDigite o valor para depositar: ").replace(',', '.'))

        if valor > 1:

            saldo += valor

            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"\nDepositado com sucesso!\nSeu novo saldo é: R$ {saldo:.2f}🤑")

        else: 
            print("\nOperação falhou! O valor informado é inválido!⚠️")

    # Sacar
        # O limite de saques é de 3 unidades. Com limite máximo de R$ 500,00 por saque.
        # Se o número de saques ultrapassar esse limite, não será possível sacar mais.
        # Se o saldo ultrapassar o limite de saques diário, não será possível sacar mais.

    elif opcao == '2':
        if numero_saques >= LIMITE_SAQUES:

            print("\nVocê atingiu o limite de saques.🥲 \nPor favor, tente outra opção!")

        else:
            valor = float(input("\nDigite o valor para sacar💰: ").replace(',', '.'))

            if valor <= 0:
                print("\nOperação falhou! O valor informado é inválido!⚠️")

            elif valor > saldo:
                print("\nSaldo insuficiente.💸") 

            # excedeu o limite de saques
            elif valor > 500: 

                print("\nOperação falhou⚠️⚠️⚠️\nO valor do saque ultrapassou o limite máximo de R$ 500,00 por transação!⚠️")


            else:
                saldo -= valor
                numero_saques += 1
                total_sacado += valor
                extrato += f"Saque: -R$ {valor:.2f}\n"
                
                print(f"\nSaque efetuado com sucesso!\n💰 Seu novo saldo é: R$ {saldo:.2f}")
                
                print(f"\nTotal sacado: R$ {total_sacado:.2f}")
                
                print(f"\nVocê já realizou {numero_saques} saques.")
                
                if numero_saques >= LIMITE_SAQUES:
                
                    print("\nVocê atingiu o limite diário de saques.🥲")

                else:
                
                    print(f"\nVocê ainda pode realizar {LIMITE_SAQUES - numero_saques} saques.")

    # Extrato

    # O extrato possui um limite de 1000 unidades.


    elif opcao == '3':

        print("\n############# EXTRATO #############")

        print(f"\nSeu saldo atual é: R$ {saldo:.2f}\n")

        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        
        print(f"\nTotal sacado: R$ {total_sacado:.2f}")
        
        print("\n################################")

    # Sair
    elif opcao == '0':

        print("\nObrigado por utilizar os nossos serviços!💘\nAté logo!😎\nSaindo👋...")
        break 

    # Se a opção não for um número inteiro entre 0 e 3
    else:
        print("\nOpção inválida⚠️.\nPor favor, selecione novamente a operação desejada!")
