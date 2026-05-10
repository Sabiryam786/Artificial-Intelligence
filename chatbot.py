import random

print("AI Chatbot started! Type 'exit' to stop")

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm fine, you?", "Doing great!", "All good!"],
    "name": ["I'm your AI chatbot"],
}

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Bye!")
        break

    found = False
    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: I don't understand yet.")
