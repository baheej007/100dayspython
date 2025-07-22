from quizmodel import model
from quizdata import question_data
from quizbrain import brain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=model(question_text,question_answer)
    question_bank.append(new_question)

quiz=brain(question_bank)
quiz.next_question()
