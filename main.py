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

