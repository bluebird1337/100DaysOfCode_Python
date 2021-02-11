class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    # TODO : 1. asking the questions
    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        res = input(f"Quiz{self.question_number } : {q.text} (True/False)")
        # TODO : 2. checking if the answer was correct
        self.check_answer(res, q.answer)

    # TODO : 3. checking if we're the end of the quiz
    def is_end(self):
        return self.question_number < len(self.question_list)


