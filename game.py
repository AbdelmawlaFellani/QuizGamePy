#!/bin/python3
import json 
import random

with open("questions.json","r", encoding="utf-8") as file:
    questions = json.load(file)

print('Welcome to league of legends Quiz')
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
q_passed=0
total_questions = len(questions)
tries = 3
quiz_questions = random.sample(questions,total_questions)

if answer.lower()=='yes':
    for q in quiz_questions:
        user_answer = input(q["question"] + " ")
        q_passed +=1
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
            tries = 3
        elif(tries > 1):
            tries -= 1
            print(f"Wrong! The correct answer is {q['answer']}.\n Guesses left {tries}")
        else:
            print(f"Wrong!\n You missed all your guesses :'/ \n The correct answer is {q['answer']}.")
            break;
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
print('Score: ',score * 10)
mark=(score/total_questions)*100
print(f"{score} out of {q_passed}")
print('Marks obtained:',mark)
print('BYE!')
exit(0)
