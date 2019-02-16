from question import Question

question_prompts = ["\nIn python, if x= 100 and y = 100, then ‘x’ and ‘y’ will..\
                   \n(a) Point at the same ‘int’ object\
                   \n(b) Point at two different ‘int’ objects\
                   \n(c) Not be created, as ‘int’ data type has not been declared \
                   while instantiating the variables\
                   \n(d) None of the above\n\n",

                    "\nIn python, if ‘x = 100’ is my first line of code, and ‘y = 100.1’ is the second line of code, then \
                   \n(a) Both x, y will point at the same object\
                   \n(b) Both x, y will point at two different objects\
                   \n(c) the variables x, y will not be created, as ‘int’ or ‘float’ data type have not been declared while instantiating the variables\
                   \n(d) None of the above\n\n",

                    "\nAny python file with a ‘.py’ extension can be a \
                   \n(a) Component\
                   \n(b) Package\
                   \n(c) Module\
                   \n(d) Library\n\n",

                    "\nA ... will always consist of a ‘__init__.py’ module.\
                   \n(a) component\
                   \n(b) package\
                   \n(c) module\
                   \n(d) library\n\n"


                    ]

# a list of questions with proper answers
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b")
]

# create a function to run our test
# taking a list <questions> as an argument
# to loop thrue all the questions
# get the user answer to each question
# check if the answer is right
# and track the results with score


def run_test(questions):
    score = 0
    for question in questions:             # goes thrue every question in questions list
        answer = input(question.prompt)    # get the user answer
        if answer == question.answer:      # check if the answer is correct
            print("\nCorrect!\n\n")
            score += 1                     # add a score if it is
        elif answer != question.answer:
            print("\nWrong answer!\n\n")

    # print the result
    print("\nYou got " + str(score) + " of " +
          str(len(questions)) + " answers correct")


# run function
run_test(questions)
