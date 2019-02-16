# The task is to build a multiple choise quiz

# We'll have two types of data here:
# 1) prompt - the actual questions
# 2) few variations of answers to that question

# We need to keep track of what is asked
# and what the answer is

# First let's create a class <question> to store
# questions prompt and qustion answers


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
