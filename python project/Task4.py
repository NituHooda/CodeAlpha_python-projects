def chatbot():
    print("🤖 Chatbot: Hello! Type something to chat. Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ").lower()

        if user_input == "exit":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        elif user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi there! 😊")
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm fine, thanks for asking! How about you?")
        elif user_input in ["bye", "goodbye"]:
            print("🤖 Chatbot: See you later! 👋")
        elif user_input in ["what's your name", "who are you"]:
            print("🤖 Chatbot: I'm a simple chatbot created with Python.")
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
