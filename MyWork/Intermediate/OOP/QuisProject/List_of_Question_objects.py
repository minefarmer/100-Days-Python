''' List of Quetion Objects.py

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.text = q_answer


'''
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)  # [<question_model.Question object at 0x0000016B4238AEC0>, <question_model.Question object at 0x0000016B42389BA0>, <question_model.Question object at 0x0000016B4238AE00>, <question_model.Question object at 0x0000016B4238AC80>, <question_model.Question object at 0x0000016B42389D50>, <question_model.Question object at 0x0000016B42389E10>, <question_model.Question object at 0x0000016B42389E70>, <question_model.Question object at 0x0000016B42389F30>, <question_model.Question object at 0x0000016B42389F90>, <question_model.Question object at 0x0000016B42389FF0>, <question_model.Question object at 0x0000016B4238A050>, <question_model.Question object at 0x0000016B4238A1D0>]


print(question_bank[0].answer)  # True
