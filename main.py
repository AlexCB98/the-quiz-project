from data import question_data
from random import shuffle

class Question:

    def __init__(self,text, answer):
        self.text   = text
        self.answer = answer

class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def show_questions(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f'Q.{self.question_number}: {current_question.text} (True / False)?: ')
        self.check_answer(u_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Correct!')
        else:
            print('Wrong!')
        print(f'The answer was: {correct_answer}')
        print(f'Current score: {self.score} / {self.question_number}')
        print('\n')


questions = []

for quest in question_data:
    questions_text   = quest['text']
    questions_answer = quest['answer']
    new_question = Question(questions_text, questions_answer)
    questions.append(new_question)

shuffle(questions)

quiz = QuizBrain(questions)
quiz.show_questions()

while quiz.still_has_questions():
    quiz.show_questions()

print('You have completed the quiz.')
print(f'Your final score was: {quiz.score} / {quiz.question_number}')