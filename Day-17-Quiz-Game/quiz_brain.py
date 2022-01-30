class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_input = input(f"Q.{self.question_number + 1} {current_question.text} True/False: ")