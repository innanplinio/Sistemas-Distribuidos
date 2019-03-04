
import Pyro4
from os import path


@Pyro4.expose
class Servidor:

    def __init__(self):
        self.__messagens = []
        self.__passw = ''
        self.__user = ''

    @property
    def messages(self):
        return self.__messagens

    @messages.setter
    def messages(self, m):
        self.__messagens.append(m)

    @property
    def passw(self):
        return self.__passw

    @passw.setter
    def passw(self, p):
        self.__passw = p

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, u):
        self.__user = u

    def enviaremail(self):
        try:
            if not path.exists(self.user):
                return "Usuário não encontrado"

            arq = open(self.user+"/emails.txt", "r")
            arq2 = open(self.user+"/passw.txt", "r")
            emails = arq.readlines()
            senha = arq2.readline()
            if senha == self.passw+"\n":
                self.messages.clear()
                for l in range(len(emails)):
                    emails[l] = emails[l].replace('\n', '')
                if len(emails) > 0:
                    for j in range(len(emails)):
                        self.messages = emails[j]
                    emails.clear()
                    return self.messages
                arq.close()
                arq2.close()

            else:
                return "Senha incorreta"


            arq.close()
            arq2.close()
        except ValueError:
            print("Error")

    def receberemail(self, message,fromm):
        try:
            if not path.exists(fromm):
                return "Destinatário não encontrado"

            arq = open(fromm+"/emails.txt", "a")
            arq.write(message)

            arq.close()
            return "Enviado com sucesso"

        except ValueError:
            print("erro")

    def verificausuario(self):
        try:
            if not path.exists(self.user):
                return "Usuário não encontrado"
            arq2 = open(self.user + "/passw.txt", "r")
            senha = arq2.readline()
            if senha == self.passw + "\n":
                return "Bem-vindo"
            else:
                return "Senha incorreta"
        except ValueError:
            print("erro")

try:

    ns = Pyro4.locateNS(hmac_key="abc")
    #  Pyro daemon. Contains server side logic and dispatches incoming remote method calls to the appropriate objects.
    daemon = Pyro4.Daemon(host="192.168.43.184")
    daemon._pyroHmacKey = "abc"
    # Register a Pyro object under the given id. Note that this object is now only known inside this daemon, it is not
    # automatically available in a name server. This method returns a URI for the registered object. Pyro checks if an
    # object is already registered, unless you set force=True. You can register a class or an object (instance) directly
    # For a class, Pyro will create instances of it to handle the remote calls according to the instance_mode
    # (set via @expose on the class). The default there is one object per session (=proxy connection). If you register
    # lan object directly, Pyro will use that single object for all remote calls.
    uri = daemon.register(Servidor)

    #  Get a proxy for a name server somewhere in the network.


    # Register a Pyro object under the given id. Note that this object is now only known inside this daemon,
    # it is not automatically available in a name server. This method returns a URI for the registered object. Pyro
    # checks if an object is already registered, unless you set force=True. You can register a class or an object (
    # instance) directly. For a class, Pyro will create instances of it to handle the remote calls according to the
    # instance_mode (set via @expose on the class). The default there is one object per session (=proxy connection). If
    # you register an object directly, Pyro will use that single object for all remote calls.
    ns.register("Serv", uri)

    print(uri)

    #  Goes in a loop to service incoming requests, until someone breaks this or calls shutdown from another thread.
    daemon.requestLoop()
except ValueError:
    print("Nao foi possivel inicializar o servidor")
    exit(0)
