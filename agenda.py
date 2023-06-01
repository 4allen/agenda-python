def menu():
    opcao = input('''
=============================================
        PROJETO AGENDA EM PYTHON
MENU:
[1]CADASTRAR CONTATO
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO NOME
[5]SAIR
=============================================
ESCOLHA UMA OPÇÃO ACIMA: 
''')
    if opcao == "1":
        cadastrarcontato()
    elif opcao =="2":
        listarcontato()
    elif opcao =="3":
        deletarcontato()
    elif opcao =="4":
        buscarnome()
    elif opcao =='5':
        sair()
    else:
        print("Insira uma opção válida!")

def cadastrarcontato():
    id = input("Escolha o id do seu contato: ")
    nome = input("Digite o nome do contato: ")
    telefone = input("Escreva o número do contato: ")
    email = input("Insira o email do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'({id};{nome};{telefone};{email})\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!!')
    except:
        print("ERRO NA GRAVAÇÃO DO CONTATO")
def listarcontato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarcontato():
    nomedeletado = input("Insira o nome para deletar o contato: ")
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range (0, len(aux)):
        if nomedeletado not in aux[i]:
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listarcontato()
    agenda.close()
    
def buscarnome():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        nome = input(f'Digite o nome a ser procurado: ')
        if nome in contato.split(";")[1]:
            print(contato)
        if nome not in contato.split(";")[1]:
            print("Contato inexistente")
        break
    agenda.close()

def sair():
    exit()

def main():

    menu()
main()