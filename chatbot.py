def reply(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm doing great, thanks for asking!"
    elif "what's your name" in message or "your name" in message:
        return "I'm your friendly chatbot!"
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm not sure how to respond to that."

print("=== Welcome to Simple Chatbot ===")
print("Type something to chat, or 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye! Take care!")
        break
    response = reply(user_input)
    print("Chatbot:", response)
