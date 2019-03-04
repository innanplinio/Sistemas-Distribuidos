import xmlrpc.client

a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))

'''Inicia a conexão com o servidor no endereço
e porta definidos e informa que a conexão
será multichamadas'''
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)


'''Procedimento de chamada das funções aritiméticas'''
multicall.add(a,b)
multicall.subtract(a,b)
multicall.multiply(a,b)
multicall.divide(a,b)

'''Inicia a multichamada'''
result = multicall()

'''Exibição do resultado através da tupla no print abaixo'''
print("a+b=%d, a-b=%d, a*b=%d, a/b=%d" % tuple(result))


