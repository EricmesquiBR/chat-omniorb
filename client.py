import sys
import threading
import CORBA, ChatApp


# function to receive the messages from the server
def receive_messages():
    ready_to_send = False
    while True:
        messages = server.getNewMessages(name)
        for message in messages:
            print(message)
            ready_to_send = False
        if not ready_to_send:
            print("Enter a message (or '-q' to quit): \n")
            ready_to_send = True

# function to send the messages to the server
def send_messages():
    while True:
        # Send a message
        message = input()#"Enter a message (or '-q' to quit): \n")
        if message.lower() == '-q':
            server.quitChat(name)
            break
        server.sendMessage(message, name)


if __name__ == '__main__':
    orb = CORBA.ORB_init(sys.argv)
    ior = input("Enter IOR: ")
    obj = orb.string_to_object(ior)
    server = obj._narrow(ChatApp.ChatServer)

    # Join the chat
    name = input("Enter your name: ")
    server.joinChat(name)
    print(f"{name} has joined the chat")

    # Start a thread to check for messages sending the client name
    threading.Thread(target=receive_messages, daemon=True).start()

    # Start a thread to send messages
    threading.Thread(target=send_messages).start()
