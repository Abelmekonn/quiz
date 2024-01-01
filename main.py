from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Quizbrain(question_bank)
while quiz.still_has_a_question():
    quiz.next_question()

print("you have completed the quiz ")
print(f"your score {quiz.score}/{quiz.question_number}")
with open("score.txt",mode="w") as score_file:
    score_file.write(f"your score {quiz.score}/{quiz.question_number}")
