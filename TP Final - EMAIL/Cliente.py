import Pyro4
import getpass
import crypt
from os import system


try:
    #  Get a proxy for a name server somewhere in the network.
    ns = Pyro4.locateNS(hmac_key="abc")

    #  Lookup the given name, returns an URI if found. Returns tuple (uri, metadata) if return_metadata is True.
    #uri = ns.lookup("Serv")

    #  Pyro proxy for a remote object. Intercepts method calls and dispatches them to the remote object.

    c = Pyro4.Proxy("PYRONAME:Serv")
    c._pyroHmacKey = "abc"
    op = 0
    print("ICEAMAIL!")
    user = input("Digite o usuario: ")
    passw = getpass.getpass(prompt="Digite a senha: ")
    passw = crypt.crypt(passw,'abc')
    system("clear")
    c.user = user
    c.passw = passw
    logar = c.verificausuario()
    print(logar)
    if logar != "Bem-vindo":
        print('Saindo...')
    else:
        while op != 3:
                op = int(input("Escolha a operação que deseja:\n1 - Checar Email\n2 - Compor email"
                               "\n3 - Sair\n Opcao: "))
                system("clear")
                if op == 3:
                    break
                if op == 1:
                    try:
                        lis = c.enviaremail()
                        if type(lis) is list:
                            for item in lis:
                                print(item)
                        else:
                            print(lis)
                        input("\nDigite qualquer tecla para continuar ")
                        system("clear")
                    except ValueError:
                        print('Erro')

                if op == 2:
                    try:
                        to = input('Destinatario:')
                        msg = input('Digite a mensagem:')
                        system("clear")
                        msg = "De: " +user+".mail Mensagem: "+msg+"\n"
                        resposta = c.receberemail(msg,to)
                        print(resposta)

                    except ValueError:
                        print('Erro')

                '''os.system('clear')'''


except ValueError:
    print("Servidor nao encontrado")
    exit(0)

