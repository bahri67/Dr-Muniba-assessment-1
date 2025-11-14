# ------------------------------------------------------------
# Algorithm 1: Simple Rule-Based Chatbot
# Author: [Your Name]
# Description:
# A basic chatbot that uses simple IF-ELSE rules.
# This version has limited responses and no dataset file.
# ------------------------------------------------------------

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello there! How are you today?"
    elif "how are you" in user_input:
        return "I’m just a bot, but I’m doing great!"
    elif "weather" in user_input:
        return "The weather seems nice — maybe go outside?"
    elif "name" in user_input:
        return "I’m Chatbot 1 — your simple rule-based assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day!"
    else:
        return "Sorry, I didn’t understand that."

def main():
    print("🤖 Simple Rule-Based Chatbot\nType 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Bye! 👋")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
