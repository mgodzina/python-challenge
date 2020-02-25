import xmlrpc.client

connection = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(connection)
print(connection.system.listMethods())
print(connection.system.methodHelp('phone'))
# "Bert" is from previous challenge
print(connection.phone("Bert"))
