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
    for i in range(4):
        My_Source.append(Question("q", "a", ["True", "False"]))
        # My_Source.append(Question("True + True", "True"))

    My_Source[0].question, My_Source[0].answer= "True + True", "True"
    My_Source[1].question, My_Source[1].answer= "True + False", "False"
    My_Source[2].question, My_Source[2].answer= "False + True", "False"
    My_Source[3].question, My_Source[3].answer= "False + False", "True"
    
    return My_Source

def Starter():
    username = input("Please Enter Your Name:")
    print("Welcome "+ username + "!")
    if input("Are you ready to start the quiz?") in ["Yes", "YES", "yes", "yES"]:
        return username

def Ask(My_Source):
    num_correct = 0
    for i in My_Source:
        print("\n\n" + i.question)
        for j in range(len(i.alternatives)):
            print(str(j+1) + ") " + i.alternatives[j])
        Ans = ""
        while not Ans: 
            # print(" \b \b")
            Ans = input()
        answer = int(Ans)
        if i.alternatives[answer-1] == i.answer:
            print("⭐ Correct! ⭐")
            num_correct += 1
        else:
            print("⚠️ Wrong! The correct answer is " + i.answer)
        
    print("\n\n ✨✨   Congrats   ✨✨\n You answred "+ str(num_correct) + " questiosn corectly!")

# username = Starter()

# Find User Information

My_Source = Initiate_Questions()
Ask(My_Source)

