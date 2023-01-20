from Question import Question

question_prompt = [
    "Colour of Apple? -\n(a)red\n(b)yellow\n(c)pink\n(d)black\n\n",
    "Colour of Banana? -\n(a)red\n(b)yellow\n(c)pink\n(d)black\n\n",
    "1 + 1 ? =\n(a)1\n(b)10\n(c)2\n(d)11\n\n",
    "What is the Capital of India? -\n(a)Kolkata\n(b)New Delhi\n(c)Mumbai\n(d)Chennai\n\n",
    "What is the National Animal of India? -\n(a)Lion\n(b)Elephant\n(c)Deer\n(d)Tiger\n\n",
    "Grand Central Terminal, Park Avenue, New York is the world's -\n(a)largest railway station\n(b)highest railway station\n(c)longest railway station\n(d)None of the above\n\n",
    "Golf player Vijay Singh belongs to which country? -\n(a)Fiji\n(b)USA\n(c)India\n(d)UK\n\n",
    "Fathometer is used to measure -\n(a)Sound intensity\n(b)Earthquakes\n(c)Rainfall\n(d)Ocean Depth\n\n"
]

answers = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "b"),
    Question(question_prompt[4], "d"),
    Question(question_prompt[5], "b"),
    Question(question_prompt[6], "a"),
    Question(question_prompt[7], "d")
]

def test(answers):
    score = 0
    for question in answers:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(answers))+" correct")

test(answers)
