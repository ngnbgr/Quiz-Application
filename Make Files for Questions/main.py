# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:41:16 2024

@author: ngnba
"""

import toml
import random
import time
import numpy as np

class Question:
    def __init__(self, Question, Answer, Alternatives):
        self.question = Question
        self.answer = Answer
        self.alternatives = Alternatives

def Starter():
    user_name = input("username: ")
    print("Welcome ❤️" + user_name + "❤️")
    print("You can quit anytime by typing \"exit\"")
    time.sleep(2)
    is_start = input("\nShall we begin? [y]/n").lower()
    match is_start:
        case "y":
            return user_name
        case "yes":
            return user_name
        case "n":
            time.sleep(1)
            raise SystemExit()
        case "n":
            time.sleep(1)
            raise SystemExit()
        case "exit":
            time.sleep(1)
            raise SystemExit()
    print("ERROR! \n Run the Program Again!")
            
            
    
        
def Init_Questions():    
    with open("questions.toml", mode="r") as fp:
        questions = toml.load(fp)
    
    total_questions = len(questions["questions"])
    print("How many questions do you want to answer?", end=(" "))
    print ("(only numbers samller than "+ str(total_questions) + ")", end=(""))
    num_question = input()
    while (not num_question.isdigit()) and int(num_question)>total_questions:
        print("⛔ NOT AVAILABLE ⛔")
        num_question = input()
    
    list_questions = np.random.choice(range(total_questions), int(num_question), replace= False)
    
    return questions, list_questions

def Ask(question, answer, options):
    print("\n\n" + question)
    count = 1
    for a in options:
        print(str(count) + ") " + options[count-1])
        count += 1
    Ans = ""
    while not Ans: 
        Ans = input().lower()
        if Ans == "exit":
            raise SystemExit()
    Answer = int(Ans)
    if options[Answer-1] == answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print("⚠️ Wrong! The correct answer is " 
              + str(options.index(answer)+1) + ") " + answer)
        return 0

def Ask_All(questions, list_questions):
    num_correct = 0
    for i in list_questions:
        question = questions["questions"]["q" + str(i)]
        answer = questions["answers"]["q" + str(i)]
        options = questions["options"]["q" + str(i)]
        num_correct += Ask(question, answer, options)
    print(print("\n\n ✨✨   Congrats   ✨✨\n You answred "+ str(num_correct) + " questiosn corectly!"))
    return


user_name = Starter()
questions, list_questions = Init_Questions()
Ask_All(questions, list_questions)
print("\n The program will get closed in 10 seconds!")
time.sleep(5)
        
    