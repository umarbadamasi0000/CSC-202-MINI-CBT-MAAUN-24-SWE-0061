
from datetime import datetime

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class Result:
    def __init__(self, score):
        self.score = score
        self.timestamp = datetime.now()

    def get_summary(self):
        return f"Score: {self.score} at {self.timestamp}"