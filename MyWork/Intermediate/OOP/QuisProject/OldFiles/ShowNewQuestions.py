''' QuisBrain 

                / question_number = 0
    attributes:/\
                 \ questions_list

             / next_question()
    methods:/\
              \ still_has_questions()

'''

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.quection_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question} (True/False): ")  # Traceback (most recent call last):
        # File "/home/rich/Desktop/CarlsHub/100-Days-Python/MyWork/Intermediate/OOP/QuisProject/main.py", line 3, in <module>
        #     from quiz_brain import QuizBrain
        # ModuleNotFoundError: No module named 'quiz_brain'