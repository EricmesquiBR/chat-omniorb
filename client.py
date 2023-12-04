import sys
import threading
import time
import tkinter as tk
from tkinter import font
import CORBA, ChatApp


# function to receive the messages from the server
def receive_messages():
    while True:
        messages = server.getNewMessages(name)
        for message in messages:
            messages_text.insert(tk.END, message + '\n')


sending_message = False


# function to send the messages to the server
def send_messages(event=None):
    global sending_message
    message = message_var.get()
    if message.lower() == '-q':
        server.quitChat(name)
        window.quit()
    elif not sending_message:
        sending_message = True
        server.sendMessage(message, name)
        message_entry.config(state='disabled')
        window.update()
        time.sleep(1)
        message_entry.config(state='normal')
        message_var.set('')
        sending_message = False


def on_closing():
    server.quitChat(name)
    window.quit()


if __name__ == '__main__':
    orb = CORBA.ORB_init(sys.argv)
    ior = input("Enter IOR: ")
    obj = orb.string_to_object(ior)
    server = obj._narrow(ChatApp.ChatServer)

    # Join the chat
    name = input("Enter your name: ")
    server.joinChat(name)

    # Set up GUI
    window = tk.Tk()
    window.geometry('500x500')  # Set initial window size

    # Set up font
    text_font = font.Font(family='Helvetica', size=14)

    messages_text = tk.Text(window, font=text_font)
    messages_text.pack(fill=tk.BOTH, expand=True)  # Make the Text widget resizable

    message_label = tk.Label(window, text=f"{name} (Enter a message or '-q' to quit):", font=text_font)
    message_label.pack()

    message_var = tk.StringVar()
    message_entry = tk.Entry(window, textvariable=message_var, font=text_font)
    message_entry.bind("<Return>", send_messages)
    message_entry.pack(fill=tk.X, expand=True)  # Make the Entry widget resizable

    # Start a thread to check for messages
    threading.Thread(target=receive_messages, daemon=True).start()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    tk.mainloop()
