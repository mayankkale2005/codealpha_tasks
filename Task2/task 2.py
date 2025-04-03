import random

class RandomQuoteApp:
    def __init__(self):
        # List of sample quotes
        self.quotes = [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
            "In the middle of every difficulty lies opportunity. – Albert Einstein",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
            "The best way to predict the future is to create it. – Peter Drucker",
            "It always seems impossible until it’s done. – Nelson Mandela",
            "Believe you can and you’re halfway there. – Theodore Roosevelt",
            "You must be the change you wish to see in the world. – Mahatma Gandhi",
            "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
            "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman"
        ]

    def display_random_quote(self):
        # Select a random quote from the list
        random_quote = random.choice(self.quotes)
        print(f"\n{random_quote}\n")

    def start(self):
        print("Welcome to the Random Quote Generator!")
        print("Press Enter to get a new quote. Type 'exit' to quit.\n")
        
        while True:
            user_input = input("Press Enter for a new quote, or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Thanks for using the Random Quote Generator! Goodbye!")
                break
            else:
                self.display_random_quote()

# Run the app
if __name__ == "__main__":
    app = RandomQuoteApp()
    app.start()
