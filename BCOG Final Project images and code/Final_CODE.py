# BEFORE RUNNING THE CODE, PLEASE DOWNLOAD THE IMAGES IN THIS FILE
import tkinter as tk
from PIL import Image, ImageTk

class SortingHatQuiz:
    def __init__(self, root):
        self.root = root
        self.init_window()

    def init_window(self):
        self.root.title("Sorting Hat Quiz")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Load the background image
        bg_image = Image.open("HP_Sorting_Background.png")
        bg_image = bg_image.resize((self.screen_width, self.screen_height))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Create a Canvas widget for the background image
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height)
        self.canvas.pack()

        # Display the background image
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Display welcome message
        self.welcome_label = tk.Label(self.root, text="Welcome to the Harry Potter Sorting Hat Quiz!", font=("Helvetica", 16))
        self.welcome_label.place(relx=0.5, rely=0.3, anchor="center")

        # Create a start button
        start_button = tk.Button(self.root, text="Start", font=("Helvetica", 14), command=self.start_quiz)
        start_button.place(relx=0.5, rely=0.5, anchor="center")

        # House logos
        self.house_logos = {
            "Gryffindor": ImageTk.PhotoImage(Image.open("Gryffindor.png").resize((300, 300))),
            "Hufflepuff": ImageTk.PhotoImage(Image.open("Hufflepuff.png").resize((300, 300))),
            "Ravenclaw": ImageTk.PhotoImage(Image.open("Ravenclaw.png").resize((300, 300))),
            "Slytherin": ImageTk.PhotoImage(Image.open("Slytherin.png").resize((300, 300))),
        }

    def start_quiz(self):
        # Destroy current widgets
        self.canvas.destroy()

        # Create questions and answer options
        self.current_question = 0
        self.questions = [
            "Which of the following colors do you like the most?",
            "Which of the following animals do you like the most?",
            "Which of the following Harry Potter characters is your favorite?",
            "Which of the following activities do you like to do in your free time?",
            "Which of the following classes do you like the most?",
            "If you were a wizard, what class would you be most interested in taking?",
            "If you had to describe yourself in one word, which one would it be?"
        ]
        self.answers = [
            ["Red", "Blue", "Green", "Yellow"],
            ["Eagle", "Lion", "Snake", "Badger"],
            ["Harry Potter", "Luna Lovegood", "Draco Malfoy", "Cedric Diggory"],
            ["Read a book", "Watch TV on the couch", "Play sports", "Work on an art project"],
            ["Math", "History", "English/reading", "Physical Education"],
            ["History of Magic", "Herbology", "Defense Against the Dark Arts", "Care of Magical Creatures"],
            ["Brave", "Loyal", "Intelligent", "Ambitious"]
        ]
        self.house_scores = {
            "Gryffindor": 0,
            "Hufflepuff": 0,
            "Ravenclaw": 0,
            "Slytherin": 0
        }

        # Display the first question
        self.display_question()

    def display_question(self):
        # Destroy old question label and answer buttons
        if hasattr(self, 'question_label'):
            self.question_label.destroy()
        if hasattr(self, 'answer_buttons'):
            for button in self.answer_buttons:
                button.destroy()

        # Display current question
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question], font=("Helvetica", 16))
        self.question_label.place(relx=0.5, rely=0.3, anchor="center")

        # Display answer buttons for the current question
        self.answer_buttons = []
        for i, answer in enumerate(self.answers[self.current_question]):
            button = tk.Button(self.root, text=answer, font=("Helvetica", 14), command=lambda ans=answer: self.process_answer(ans))
            button.place(relx=0.5, rely=0.4 + i * 0.1, anchor="center")
            self.answer_buttons.append(button)

    def process_answer(self, answer):
        # Update house scores based on the answer
        if answer == "Red" or answer == "Lion" or answer == "Harry Potter" or answer == "Play sports" or answer == "Brave":
            self.house_scores["Gryffindor"] += 1
        elif answer == "Yellow" or answer == "Badger" or answer == "Cedric Diggory" or answer == "Work on an art project" or answer == "Loyal":
            self.house_scores["Hufflepuff"] += 1
        elif answer == "Blue" or answer == "Eagle" or answer == "Luna Lovegood" or answer == "Read a book" or answer == "Intelligent":
            self.house_scores["Ravenclaw"] += 1
        elif answer == "Green" or answer == "Snake" or answer == "Draco Malfoy" or answer == "Watch TV on the couch" or answer == "Ambitious":
            self.house_scores["Slytherin"] += 1

        # Move to the next question or display the result
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.display_result()

    def display_result(self):
        # Determine the house with the highest score
        sorted_houses = sorted(self.house_scores.items(), key=lambda x: x[1], reverse=True)
        winner_house = sorted_houses[0][0]
        
        # Destroy current widgets
        self.question_label.destroy()
        for button in self.answer_buttons:
            button.destroy()
        self.welcome_label.destroy()

        # Display the result and corresponding house logo
        result_label = tk.Label(self.root, text=f"Congratulations! You have been placed in {winner_house} house!", font=("Helvetica", 16))
        result_label.place(relx=0.5, rely=0.4, anchor="center")

        house_logo = self.house_logos[winner_house]
        house_logo_label = tk.Label(self.root, image=house_logo)
        house_logo_label.place(relx=0.5, rely=0.6, anchor="center")

def main():
    # Create the main window
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Set fullscreen mode
    sorting_hat_quiz = SortingHatQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
