import sys
import CORBA, ChatApp, ChatApp__POA


class ChatServer_i(ChatApp__POA.ChatServer):
    def __init__(self):
        self.clients = []

    def sendMessage(self, message, sender):
        print(f"Received message from {sender}: {message}")
        for client in self.clients:
            client.receiveMessage(message, sender)

    def receiveMessage(self):
        # Implementation as needed
        return ""



orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = ChatServer_i()
poa.activate_object(servant)

print(orb.object_to_string(servant._this()))

poa._get_the_POAManager().activate()
orb.run()
