import sys
import CORBA, ChatApp

orb = CORBA.ORB_init(sys.argv)
ior = input("Enter IOR: ")
obj = orb.string_to_object(ior)
server = obj._narrow(ChatApp.ChatServer)

# Join the chat
name = input("Enter your name: ")
server.joinChat(name)

while True:
    # Send a message
    message = input("Enter a message (or 'quit' to quit): ")
    if message.lower() == 'quit':
        server.quitChat(name)
        break
    server.sendMessage(message, name)

    # Retrieve and print messages
    messages = server.getMessages()
    for message in messages:
        print(message)
