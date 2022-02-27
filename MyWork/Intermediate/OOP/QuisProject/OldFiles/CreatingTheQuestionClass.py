'''
Question
                /text "2+3=5"
    attributes:/\
                 \answer "True"

'''
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("stucgh", "False")
print(new_q.text)  # stucgh
