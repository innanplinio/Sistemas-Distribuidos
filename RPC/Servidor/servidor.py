from xmlrpc.server import SimpleXMLRPCServer
'''Funções responsáveis por realizar as operações aritiméticas de Soma, 
Subtração, Multiplicação, divisão entre dois valores recebidos pelo cliente 
e retornar o resultado da operação'''
def add(x,y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

print("Trabalho de Sistemas Distribuídos – Professora Carla Lara.")

'''Inicialização do servidor na rede local e a porta de comunicação 8000'''
server = SimpleXMLRPCServer(("localhost", 8000))
print("Aguardando conexão na porta 8000")

'''Define que a entrada será multichamada, ou seja, 
várias funções serão acionadas pelo cliente'''
server.register_multicall_functions()

'''Registro das funções de soma, subtração, multiplicação e divisão'''
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')

'''Continua no loop do server'''
server.serve_forever()
#Referência: https://docs.python.org/2/library/xmlrpclib.html





