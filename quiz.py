import tkinter as tk
from tkinter import messagebox

# Define a list of quiz questions with options and correct answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale"],
        "answer": "Blue Whale",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        self.correct_answer_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.correct_answer_label.pack()

        for i in range(3):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack()

        self.next_question()

    def next_question(self):
        if self.current_question < len(quiz_data):
            question_data = quiz_data[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(3):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.correct_answer_label.config(text="")  # Clear previous correct answer
            self.current_question += 1
        else:
            self.show_result()

    def check_answer(self, selected_option):
        question_data = quiz_data[self.current_question - 1]
        correct_answer = question_data["answer"]
        selected_answer = question_data["options"][selected_option]

        if selected_answer == correct_answer:
            self.score += 1
            self.correct_answer_label.config(text="Correct!", fg="green")
        else:
            self.correct_answer_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")

        if self.current_question < len(quiz_data):
            self.next_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(quiz_data)}!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
