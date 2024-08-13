# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib as mpl

class Question:
    def __init__(self, Question, Answer, Alternatives):
        self.question = Question
        self.answer = Answer
        self.alternatives = Alternatives

def Initiate_Questions():
    My_Source = []
    for i in range(8):
        My_Source.append(Question("q", "a", 
                                  np.random.shuffle(["True", "False"])))
        # My_Source.append(Question("True + True", "True"))

    My_Source[0].question, My_Source[0].answer= "True + True", "True"
    My_Source[1].question, My_Source[1].answer= "True + False", "False"
    My_Source[2].question, My_Source[2].answer= "False + True", "False"
    My_Source[3].question, My_Source[3].answer= "False + False", "True"
    My_Source[4].question, My_Source[4].answer= "5>=5", "True"
    My_Source[5].question, My_Source[5].answer= "4>-4", "True"
    My_Source[6].question, My_Source[6].answer= "3>7", "False"
    My_Source[7].question, My_Source[7].answer= "-1<-5", "False"
    
    # for j in range(4):
    #     My_Source.append(Question('q', 'a', ['0', '1', '2', '3']))
    
    # My_Source[8].question, My_Source[8].answer= "False + False", "True"
    
    return My_Source

def Starter(num_source):
    username = input("Please Enter Your Name:")
    print("Welcome "+ username + "!")
    if input("Are you ready to start the quiz?") in ["Yes", "YES", "yes", "yES"]:
        print("\n\nYou can type \"exit\" to close the program.")
        
        print("How many questions do you want to answer?", end=(" "))
        print ("(only numbers samller than "+ str(num_source) + ")", end=(""))
        num_question = input()
        while (not num_question.isdigit()) and int(num_question)>num_source:
            print("⛔ NOT AVAILABLE ⛔")
            num_question = input()
        return username, int(num_question)
    else:
        raise SystemExit()
    

def Ask(Source, num_question):
    My_Source = np.random.choice(Source, num_question, replace=False)
    num_correct = 0
    for i in My_Source:
        print("\n\n" + i.question)
        for j in range(len(i.alternatives)):
            print(str(j+1) + ") " + i.alternatives[j])
        Ans = ""
        while not Ans: 
            Ans = input()
            if Ans in ["exit", "Exit", "EXIT", "eXIT"]:
                raise SystemExit()
        answer = int(Ans)
        if i.alternatives[answer-1] == i.answer:
            print("⭐ Correct! ⭐")
            num_correct += 1
        else:
            print("⚠️ Wrong! The correct answer is " + i.answer)
        
    print("\n\n ✨✨   Congrats   ✨✨\n You answred "+ str(num_correct) + " questiosn corectly!")
# x= [i for i in range(5)]
# np.random.shuffle(x)
# print(x)
My_Source = Initiate_Questions()
username, num_question = Starter(len(My_Source))

# Find User Information

Ask(My_Source, num_question)

