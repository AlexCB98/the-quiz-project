from data import question_data

class Question:

    def __init__(self,text, answer):
        self.text   = text
        self.answer = answer

questions = []

for quest in question_data:
    questions_text   = quest['text']
    questions_answer = quest['answer']
    new_question = Question(questions_text, questions_answer)
    questions.append(new_question)

class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list

    def show_questions(self):

        current_question = self.question_list[self.question_number]
        answer = input(f'Q.{self.question_number}: {current_question.text} (True / False)?: ')