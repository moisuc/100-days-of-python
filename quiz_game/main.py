from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank: list[Question] = []
for q_data in question_data:
    question_bank.append(Question(q_data['text'], q_data['answer']))
quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
quiz_brain.finish()
