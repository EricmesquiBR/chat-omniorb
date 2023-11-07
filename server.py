# chat_server.py
import CORBA
import ChatApp

class ChatServer_i(ChatApp.ChatServer):
    def __init__(self):
        self.clients = []

    def sendMessage(self, message, sender):
        for client in self.clients:
            client.receiveMessage(message, sender)

    def receiveMessage(self):
        # Implementation as needed
        pass

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

server = ChatServer_i()
poa.activate_object(server)

# Obtain a reference to the server object
obj = poa.id_to_reference(poa.servant_to_id(server))

# Export the server reference
ior = orb.object_to_string(obj)

# Print the IOR (Interoperable Object Reference) for clients to connect
print("Chat Server IOR:", ior)

# Run the ORB event loop
orb.run()
