import toml

with open("questions.toml", mode="r") as fp:
    questions = toml.load(fp)

questions["questions"]["q1"] = "True + False"
questions["questions"]["q2"] = "False + True"
questions["questions"]["q3"] = "False + False"

questions["answers"]["q1"] = "False"
questions["answers"]["q2"] = "False"
questions["answers"]["q3"] = "True"

questions["options"]["q1"] = ["True","False"]
questions["options"]["q2"] = ["True","False"]
questions["options"]["q3"] = ["True","False"]

with open("questions.toml", mode="w") as fp:
    toml.dump(questions, fp)

questions["questions"]["q4"] = "How do you insert COMMENTS in Python code?"
questions["answers"]["q4"] = "# This is comment"
questions["options"]["q4"] = ["\\This is comment", "\*This is comment*\ ", "# This is comment"]

questions["questions"]["q5"] = "Which one is NOT a legal variable name?"
questions["answers"]["q5"] = "_myvar"
questions["options"]["q5"] = ["_myvar", "Myvar", "my-var", "my_var"]

questions["questions"]["q6"] = "How do you create a variable with the numeric value 5?"
questions["answers"]["q6"] = "Both answers are correct"
questions["options"]["q6"] = ["x = 5", "x = int(5)", "Both answers are correct"]

questions["questions"]["q7"] = "What is the correct file extension for Python files?"
questions["answers"]["q7"] = ".py"
questions["options"]["q7"] = [".pt", ".py", ".pyt", ".pyth"]

with open("questions.toml", mode="w") as fp:
    toml.dump(questions, fp)