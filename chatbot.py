def chatbot():
    print("Basic Chatbot")
    print("Type hello, how are you, help, or bye.")

    while True:
        user_message = input("You: ").strip().lower()

        if user_message in ("hello", "hi", "hey"):
            print("Bot: Hi! How can I help you?")
        elif user_message == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_message == "help":
            print("Bot: You can say hello, ask how I am, or type bye to exit.")
        elif user_message in ("bye", "exit", "quit"):
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()
