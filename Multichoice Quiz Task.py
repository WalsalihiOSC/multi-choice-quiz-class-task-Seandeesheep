# 01/04/22

# module
from tkinter import *


class MultiChoiceQuizGUI:

    def __init__(self, parent, quiz_questions):
        self.q = quiz_questions
        self.q_n = 0

        # initialising frame
        self.main_frame = Frame(parent, width=400, height=400)

        # multichoice variable
        self.choice = StringVar()
        self.choice.set('')

        # initialising labels
        self.q_label = Label(self.main_frame, text=f"{self.q_n + 1}. {self.q.get_q()[self.q_n]}", padx=20, pady=5)

        # initialising buttons
        self.multichoice_button = []
        for i in range(len(self.q.get_ans()[self.q_n])):
            self.multichoice_button.append(
                Radiobutton(self.main_frame, text=self.q.get_ans()[self.q_n][i], value=self.q.get_ans()[self.q_n][i],
                            variable=self.choice))
        confirm_button = Button(self.main_frame, text="Confirm", command=self.check_answer)

        # widget grid
        self.main_frame.grid(sticky=N)
        self.q_label.grid(sticky=NSEW, row=0, column=0)
        for i in range(len(self.multichoice_button)):
            self.multichoice_button[i].grid(row=i + 1, sticky=NSEW, padx=20, pady=5)
        confirm_button.grid(row=2 + len(self.multichoice_button), pady=10)

    def redisplay(self):
        self.q_label.configure(text=f"{self.q_n + 1}. {self.q.get_q()[self.q_n]}", padx=20, pady=5)
        for i in range(len(self.multichoice_button)):
            self.multichoice_button[i].configure(text=self.q.get_ans()[self.q_n][i], value=self.q.get_ans()[self.q_n][i])

    def check_answer(self):
        if self.q_n >= len(self.q.get_q())-1:
            print('done')
        elif self.choice.get() == self.q.get_ans()[self.q_n][self.q.get_ans_index()[self.q_n]]:
            self.q_n += 1
            self.redisplay()



class QuizQuestions:

    def __init__(self, questions, answers, correct_answers):
        self.questions = questions
        self.answers = answers
        self.correct_answers = correct_answers

    def get_q(self):
        return self.questions

    def get_ans(self):
        return self.answers

    def get_ans_index(self):
        return self.correct_answers


# CONSTANTS
QUIZ_1 = ["What is the capital of New Zealand", "What is the capital of China", "What is the capital of Cambodia"]
ANSWERS_1 = [["Wellington", "Auckland", "Dunedin", "Queenstown"],
             ["Shanghai", "Beijing", "Hong Kong", "Taiwan"],
             ["Phnom Penh", "Angkor", "Samraong", "Krong Siem Reap"]]
CORRECT_ANSWERS_1 = [0, 1, 0]

# mainloop
root = Tk()
quiz = QuizQuestions(QUIZ_1, ANSWERS_1, CORRECT_ANSWERS_1)
MultiChoiceQuizGUI(root, quiz)

root.mainloop()
