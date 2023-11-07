# chat_client.py
import CORBA
import ChatApp

class ChatClient_i(ChatApp.ChatClient):
    def receiveMessage(self, message, sender):
        print(f"Received message from {sender}: {message}")

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
ior = input("Enter the Chat Server IOR: ")

# Resolve the server object reference
obj = orb.string_to_object(ior)
server = obj._narrow(ChatApp.ChatServer)

if server is None:
    print("Object reference is not a valid Chat Server")
    sys.exit(1)

# Create and activate the client servant
client = ChatClient_i()
poa = orb.resolve_initial_references("RootPOA")
poa.activate_object(client)

# Register the client with the server
server.registerClient(client)

# Interact with the server as needed
# (e.g., send and receive messages)

# Run the ORB event loop
orb.run()
