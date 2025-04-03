import tkinter as tk
import random
import json

# Sample Data
quotes = [
    "Learning a new language is like gaining a new soul.",
    "The limits of my language mean the limits of my world. - Ludwig Wittgenstein",
    "A new language is a new life.",
    "The more that you read, the more things you will know. - Dr. Seuss",
    "To have another language is to possess a second soul. - Charlemagne"
]

# Simple Vocabulary List for Lessons
lessons = {
    "Spanish": [
        {"word": "Hola", "meaning": "Hello"},
        {"word": "Adiós", "meaning": "Goodbye"},
        {"word": "Gracias", "meaning": "Thank you"},
        {"word": "Por favor", "meaning": "Please"},
        {"word": "Sí", "meaning": "Yes"}
    ],
    "French": [
        {"word": "Bonjour", "meaning": "Hello"},
        {"word": "Au revoir", "meaning": "Goodbye"},
        {"word": "Merci", "meaning": "Thank you"},
        {"word": "S'il vous plaît", "meaning": "Please"},
        {"word": "Oui", "meaning": "Yes"}
    ]
}

# Initialize User Progress (JSON File)
user_progress = {
    "level": 1,
    "points": 0,
    "lessons_completed": 0,
    "achievements": []
}

# Save user progress to file
def save_progress():
    with open("user_progress.json", "w") as f:
        json.dump(user_progress, f)

# Load user progress from file
def load_progress():
    global user_progress
    try:
        with open("user_progress.json", "r") as f:
            user_progress = json.load(f)
    except FileNotFoundError:
        pass

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Function to display a random quote
def show_quote():
    quote_label.config(text=get_random_quote())

# Function to start the lesson
def start_lesson():
    global current_lesson, current_word_index
    current_lesson = lessons.get("Spanish", [])  # Set Spanish as default
    current_word_index = 0
    show_word()

# Function to show the next word in the lesson
def show_word():
    global current_word_index
    if current_word_index < len(current_lesson):
        word = current_lesson[current_word_index]["word"]
        meaning = current_lesson[current_word_index]["meaning"]
        lesson_label.config(text=f"Word: {word}\nMeaning: {meaning}")
        current_word_index += 1
    else:
        lesson_label.config(text="Congratulations! You've completed this lesson.")
        user_progress["lessons_completed"] += 1
        user_progress["points"] += 10
        save_progress()

# Quiz Game Section
def start_quiz():
    global current_quiz_index
    current_quiz_index = 0
    show_quiz_question()

def show_quiz_question():
    global current_quiz_index
    if current_quiz_index < len(current_lesson):
        word = current_lesson[current_quiz_index]["word"]
        answer_entry.config(state="normal")
        quiz_label.config(text=f"What is the meaning of '{word}'?")
        submit_button.config(state="normal")
    else:
        quiz_label.config(text="Quiz Completed! Well done.")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")

# Check Answer in Quiz Game
def check_answer():
    global current_quiz_index
    user_answer = answer_entry.get().lower()
    correct_answer = current_lesson[current_quiz_index]["meaning"].lower()
    if user_answer == correct_answer:
        user_progress["points"] += 5
        achievement_label.config(text="Correct! Points added.")
    else:
        achievement_label.config(text=f"Incorrect! The correct answer was: {correct_answer}")
    
    current_quiz_index += 1
    answer_entry.delete(0, 'end')
    show_quiz_question()

# Main GUI Window
root = tk.Tk()
root.title("Language Learning App")

# Quote Section
quote_label = tk.Label(root, text=get_random_quote(), font=("Helvetica", 14), wraplength=400, justify="center")
quote_label.pack(pady=20)

quote_button = tk.Button(root, text="New Quote", command=show_quote, font=("Helvetica", 12))
quote_button.pack(pady=10)

# Lesson Section
lesson_label = tk.Label(root, text="Welcome to your language lesson!", font=("Helvetica", 14), wraplength=400, justify="center")
lesson_label.pack(pady=20)

lesson_button = tk.Button(root, text="Start Lesson", command=start_lesson, font=("Helvetica", 12))
lesson_button.pack(pady=10)

# Quiz Game Section
quiz_label = tk.Label(root, text="Get ready for the quiz!", font=("Helvetica", 14), wraplength=400, justify="center")
quiz_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer, font=("Helvetica", 12))
submit_button.pack(pady=10)

# Achievement Section
achievement_label = tk.Label(root, text="Achievements: ", font=("Helvetica", 12), wraplength=400, justify="center")
achievement_label.pack(pady=20)

# Track User Progress Section
progress_label = tk.Label(root, text=f"Level: {user_progress['level']}  Points: {user_progress['points']}  Lessons Completed: {user_progress['lessons_completed']}", font=("Helvetica", 12), wraplength=400, justify="center")
progress_label.pack(pady=10)

# Load progress at start
load_progress()

# Start the app
root.mainloop()
