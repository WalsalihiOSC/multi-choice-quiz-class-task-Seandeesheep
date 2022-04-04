# 01/04/22

# module
from tkinter import *


class MultiChoiceQuizGUI:

    def __init__(self, parent, quiz_questions):
        # initialising frame
        main_frame = Frame(parent, width=400, height=400)

        # initialising labels
        question_label = Label(main_frame, text=1, padx=20, pady=5)

        # widget grid
        main_frame.grid(sticky=N)
        question_label.grid(sticky=NSEW, row=0, column=0)


class QuizQuestions:

    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers


# mainloop
root = Tk()

quiz = QuizQuestions()
MultiChoiceQuizGUI(root, quiz)
quiz_1 = ["What is the capital of New Zealand", "What is the capital of China", "What is the capital of Cambodia"]
answer_1 = ["Wellington", "Beijing", "Phnom Penh"]

root.mainloop()
