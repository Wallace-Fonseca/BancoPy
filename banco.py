from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('\n')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-=-= ATM =-=-=-=-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-= Fox Bank =-==-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')


    print('Selecione uma opção no menu:')
    print('   1 - Criar Conta.')
    print('   2 - Efetuar Saque.')
    print('   3 - Efetuar Deposito.')
    print('   4 - Efetuar Tranferencia.')
    print('   5 - Listar Contas.')
    print('   6 - Sair do Sistema.\n')

    opcao: int = int(input('Informe a opção desejada: '))

    if opcao == 1:
        print('\n')
        criar_conta()
    elif opcao ==2:
        print('\n')
        efetuar_saque()
    elif opcao ==3:
        print('\n')
        efetuar_deposito()
    elif opcao == 4:
        print('\n')
        efetuar_tranferencia()
    elif opcao == 5:
        print('\n')
        listar_contas()
    elif opcao == 6:
        print('\n')
        print('Obrigado pela preferencia.')
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('\n')
        print('Opção Invalida. Tente Novamente')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do Cliente:')
    nome: str = str(input('   Nome do Cliente: '))
    email: str = str(input('   Email do Cliente: '))
    cpf: str = str(input('   CPF do Cliente: '))
    data_nascimento: str = input('   Data de nascimento do Cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta Criada com Sucesso!\n')
    print('=-=-=-=-= Dados da Conta: =-=-=-=-=')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'A conta {numero} não existe.')

    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da conta para deposito: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))

            conta.depositar(valor)
        else:
            print(f'A conta {numero} não existe.')
    else:
        print('Ainda não existe contas cadastradas.')
    sleep(2)
    menu()


def efetuar_tranferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o numero da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número de conta destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da tranferencia: '))

                conta_o.tranferir(conta_d, valor)

            else:
                print(f'A conta destino {numero_d} não foi encontrada!')
        else:
            print(f'A sua conta com o numero {numero_o} não foi encontrada!')
    else:
        print('Ainda não existe contas cadastradas!')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('=-=-=-=-= Listagem de Contas: =-=-=-=-=')

        for conta in contas:
            print(conta)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            sleep(1)

    else:
        print('Não existe contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> None:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()
