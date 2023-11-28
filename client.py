import sys
import threading
import CORBA, ChatApp


# function to receive the messages from the server
def receive_messages():
    last_received_message = None
    while True:
        messages = server.getMessages()
        if messages:
            newest_message = messages[-1]
            if last_received_message != newest_message:
                last_received_message = newest_message
                print(newest_message)

# function to send the messages to the server
def send_messages():
    while True:
        # Send a message
        message = input("Enter a message (or '-q' to quit): \n")
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

    # Start a thread to check for messages
    threading.Thread(target=receive_messages, daemon=True).start()

    # Start a thread to send messages
    threading.Thread(target=send_messages).start()