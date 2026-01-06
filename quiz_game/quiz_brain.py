from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    def finish(self) -> None:
        print("You completed the quest")
        print(f"Your score is: {self.score}/{self.question_number}")
