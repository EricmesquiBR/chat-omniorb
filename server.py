import sys
import datetime
import os
import logging
import CORBA, ChatApp, ChatApp__POA

# Set up logging and log the start of the server
logging.basicConfig(filename='chat.log', level=logging.INFO)
logging.info('Server started at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class ChatServer_i(ChatApp__POA.ChatServer):
    def __init__(self):
        self.clients = []
        self.messages = []

    def sendMessage(self, message, sender):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {sender}: {message}"
        self.messages.append(log_message)
        logging.info(log_message)  # Log the message
        print(log_message)
        for client in self.clients:
            client.receiveMessage(message, sender)

    def receiveMessage(self):
        #for each new message its loaded this function is called to get the message on the client side
        return "paia"

    def joinChat(self, name):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        join_message = f"{timestamp} - {name} has joined the chat"
        self.messages.append(join_message)
        logging.info(join_message)  # Log the join event
        print(join_message)

    def quitChat(self, name):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        quit_message = f"{timestamp} - {name} has left the chat"
        self.messages.append(quit_message)
        logging.info(quit_message)  # Log the quit event
        print(quit_message)

    def getMessages(self):
        return self.messages




orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = ChatServer_i()
poa.activate_object(servant)

print(orb.object_to_string(servant._this()))

poa._get_the_POAManager().activate()
orb.run()
