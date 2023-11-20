import sys
import CORBA, ChatApp

orb = CORBA.ORB_init(sys.argv)
#digit the object ior
print("Enter the object ior: ")
ior = str(input())
obj = orb.string_to_object(ior)
server = obj._narrow(ChatApp.ChatServer)


# Send a message
server.sendMessage("Hello, server!", "Client")
