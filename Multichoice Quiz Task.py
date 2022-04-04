# 01/04/22

# module
from tkinter import *


class MultiChoiceQuizGUI:
    """
    Creates a multi choice quiz widget
    """
    def __init__(self, parent, quiz_questions):
        """
        initialises the main frame with the multi choice question widgets
        """
        self.q = quiz_questions
        self.q_n = 0

        # initialising frame
        self.main_frame = Frame(parent, width=400, height=400)

        # multichoice variable
        self.choice = StringVar()
        self.choice.set('')

        # initialising labels
        self.q_label = Label(self.main_frame, text=f"{self.q_n + 1}. {self.q.get_q()[self.q_n]}", padx=20, pady=5)
        self.congratz_label = Label(self.main_frame, text="Congratulations, you've done it!")

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
        """
        displays a new set of question and multi choice answers
        """
        self.q_label.configure(text=f"{self.q_n + 1}. {self.q.get_q()[self.q_n]}", padx=20, pady=5)
        for i in range(len(self.multichoice_button)):
            self.multichoice_button[i].configure(text=self.q.get_ans()[self.q_n][i], value=self.q.get_ans()[self.q_n][i])

    def check_answer(self):
        """
        checks if the answer selected is correct
        """
        if self.choice.get() == self.q.get_ans()[self.q_n][self.q.get_ans_index()[self.q_n]]:
            if self.q_n < len(self.q.get_q())-1:
                self.q_n += 1
                self.redisplay()
            else:
                self.congratz_label.grid(row=3 + len(self.multichoice_button), pady=5)



class QuizQuestions:
    """
    Compiles all the info of multi choice quiz. Such as the questions, answers and the answer index
    """
    def __init__(self, questions, answers, correct_answers):
        """
        initialises the parameters
        """
        self.questions = questions
        self.answers = answers
        self.correct_answers = correct_answers

    def get_q(self):
        """
        returns the question list
        """
        return self.questions

    def get_ans(self):
        """
        returns the multi choice answer list
        """
        return self.answers

    def get_ans_index(self):
        """
        returns the index list for the right answers
        """
        return self.correct_answers


# CONSTANTS
QUIZ_1 = ["What is the capital of New Zealand",
          "What is the capital of China",
          "What is the capital of Cambodia",
          "What is the capital of America",
          "What is the capital of Algeria"
          ]
ANSWERS_1 = [["Wellington", "Auckland", "Dunedin", "Queenstown"],
             ["Shanghai", "Beijing", "Hong Kong", "Taiwan"],
             ["Phnom Penh", "Angkor", "Samraong", "Krong Siem Reap"],
             ["New York", "Chicago", "Washington DC", "San Francisco"],
             ["Setif", "Algiers", "Annaba", "Oran"]]
CORRECT_ANSWERS_1 = [0, 1, 0, 2, 1]

# mainloop
root = Tk()
quiz = QuizQuestions(QUIZ_1, ANSWERS_1, CORRECT_ANSWERS_1)
MultiChoiceQuizGUI(root, quiz)

root.mainloop()
