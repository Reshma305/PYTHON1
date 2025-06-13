questions = ("How many elements are in the periodic table?: ",
             "What is the chemical symbol for gold?: ",
             "Which organ in the human body is primarily responsible for detoxification?: ",
             "What is the process by which plants make their own food using sunlight?: ",
             "What is the name of the pigment that gives plants their green color and absorbs sunlight?: ")
options = (("A. 116","B.117","C.118","D.119"),
           ("A. Go ","B. Au","C.Ag","D. Gd"),
           ("A. Kidney ","B. Liver","C.  Pancreas","D. Lung"),
           ("A.Respiration ","B.Germination","C.Photosynthesis","D. Fermentation")
           ("A.Hemoglobin ","B. Chlorophyll","C.Melanin","D.Carotene"))


answers = ("C","B","B","C","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1 