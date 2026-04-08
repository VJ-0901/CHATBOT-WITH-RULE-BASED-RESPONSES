import re
import random
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.user_name = None
        self.running = True

    # Time-based greeting
    def get_greeting(self):
        hour = datetime.now().hour
        if hour < 12:
            return "Good morning"
        elif hour < 17:
            return "Good afternoon"
        else:
            return "Good evening"

    # Main response function
    def respond(self, user_input):
        user_input = user_input.lower().strip()

        # RULES (pattern → response)
        rules = [
            # Greeting
            (r'\b(hi|hello|hey)\b',
             [f"{self.get_greeting()}! How can I assist you today?",
              "Hello! What can I help you with?",
              "Hey! How can I help you?"]),

            # Name input
            (r'my name is (\w+)', None),

            # Ask name
            (r'\b(what is my name|do you remember my name)\b', None),

            # Identity
            (r'\b(who are you|what are you)\b',
             ["I am a rule-based chatbot created using Python.",
              "I am your AI assistant built for learning purposes."]),

            # AI
            (r'\b(what is ai|artificial intelligence)\b',
             ["Artificial Intelligence is the ability of machines to think and learn like humans."]),

            # ML
            (r'\b(machine learning|ml)\b',
             ["Machine Learning is a subset of AI where systems learn from data."]),

            # Help
            (r'\b(help|what can you do)\b',
             ["I can answer basic AI questions, remember your name, and chat with you.",
              "Try asking me about AI, ML, or tell me your name!"]),

            # Mood
            (r'\b(how are you)\b',
             ["I'm doing great! Thanks for asking 😊",
              "All systems are running perfectly!"]),

            # Positive replies
            (r'\b(good|fine|great|awesome)\b',
             ["That's great to hear! 😊",
              "Awesome! Keep it up!"]),

            # Thanks
            (r'\b(thanks|thank you)\b',
             ["You're welcome!",
              "Happy to help! 😊"]),

            # Exit
            (r'\b(bye|exit|quit)\b',
             ["Goodbye! Have a nice day 👋"])
        ]

        # Pattern matching
        for pattern, response in rules:
            match = re.search(pattern, user_input)

            if match:
                # Store name
                if pattern == r'my name is (\w+)':
                    self.user_name = match.group(1)
                    return f"Nice to meet you, {self.user_name}! 😊"

                # Recall name
                if pattern == r'\b(what is my name|do you remember my name)\b':
                    if self.user_name:
                        return f"Your name is {self.user_name}."
                    else:
                        return "I don't know your name yet. Tell me using 'My name is ...'"

                return random.choice(response)

        return "Sorry, I didn't understand that. Can you rephrase?"

    # Chat loop
    def start_chat(self):
        print("===== Rule-Based Chatbot =====")
        print("Type 'bye' to exit\n")

        while self.running:
            user_input = input("You: ")

            if re.search(r'\b(bye|exit|quit)\b', user_input.lower()):
                print("Chatbot: Goodbye! 👋")
                break

            response = self.respond(user_input)
            print("Chatbot:", response)


# Run chatbot
if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()