# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:41:16 2024

@author: ngnba
"""

import toml
import random

class Question:
    def __init__(self, Question, Answer, Alternatives):
        self.question = Question
        self.answer = Answer
        self.alternatives = Alternatives
        
def Init_Questions(num_question):
    with open("questions.toml", mode="r") as fp:
        questions = toml.load(fp)
    
    list_questions = random.choice(range(len(questions["questions"])), num_question)
    
    return questions, list_questions

def Ask(question, answer, options):
    print("\n\n" + question)
    count = 1
    for a in options:
        print(count + " ) " + options[count-1])
        count += 1
    Ans = ""
    while not Ans: 
        Ans = input()
        if Ans in ["exit", "Exit", "EXIT", "eXIT"]:
            raise SystemExit()
    answer = int(Ans)
    if options[answer-1] == answer:
        print("⭐ Correct! ⭐")
        return True
    else:
        print("⚠️ Wrong! The correct answer is " 
              + str(options.index(answer)+1) + ") " + i.answer)
        return False

def Ask_All(questions, list_questions):
    # for i in list_questions:
        
    