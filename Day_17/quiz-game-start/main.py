from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for each_data in question_data:
    question = Question(each_data["question"], each_data["correct_answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():# if quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")