# ------------------------------------------------------------
# Algorithm 2: Expert Chatbot (Improved Rule-Based AI)
# Author: [Your Name]
# Description:
# A more advanced chatbot that uses a dataset of rules (CSV).
# Uses forward-chaining logic and keyword matching.
# ------------------------------------------------------------

import csv

# Load rules from dataset2.csv
rules = []
with open("dataset2.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rules.append({"pattern": row["pattern"].lower(), "response": row["response"]})

def match_rule(user_input):
    """
    Matches user input to a rule pattern.
    Returns the corresponding response if found.
    """
    for rule in rules:
        if rule["pattern"] in user_input:
            return rule["response"]
    return "I'm not sure how to respond to that."

def main():
    print("🤖 Expert Chatbot (Rule-Based AI)\nType 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! 👋")
            break

        response = match_rule(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
