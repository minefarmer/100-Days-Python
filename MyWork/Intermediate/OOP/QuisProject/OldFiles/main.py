from MyWork.Intermediate.OOP.QuisProject.OldFiles.question_model import Question
from MyWork.Intermediate.OOP.QuisProject.OldFiles.data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

#  Lesson 160

while quiz.still_has_questions():  # if quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: 10/{len(question_bank)}")

# (OR)  print(f"Your final score was: 10/{quiz.question_number}")
