import sys
import CORBA, ChatApp, ChatApp__POA


class ChatServer_i(ChatApp__POA.ChatServer):
    def __init__(self):
        self.clients = []
        self.messages = []

    def sendMessage(self, message, sender):
        self.messages.append(f"{sender}: {message}")
        print(f"{sender}: {message}")
        for client in self.clients:
            client.receiveMessage(message, sender)

    def receiveMessage(self):
        # Implementation as needed
        return ""

    def joinChat(self, name):
        self.messages.append(f"{name} has joined the chat")
        print(f"{name} has joined the chat")

    def quitChat(self, name):
        self.messages.append(f"{name} has left the chat")
        print(f"{name} has left the chat")

    def getMessages(self):
        return self.messages


orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = ChatServer_i()
poa.activate_object(servant)

print(orb.object_to_string(servant._this()))

poa._get_the_POAManager().activate()
orb.run()
