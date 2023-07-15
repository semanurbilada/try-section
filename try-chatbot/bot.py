from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# WhatsApp chats ile training process yapılabilir!

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, new friend 😇",
])
trainer.train([
    "What are you, a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit")
print("\nYou can exit with these commands:", exit_conditions, "\n")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🌸 {chatbot.get_response(query)}")