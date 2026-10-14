# Python quiz game of The Brokenwood Mysteries

questions = ("What is the nationality and profession of Dr. Gina Kadinsky?: ",
             "Which specific musical artist is Mike Shepherd frequently listening to on cassette tapes in his vintage car?: ",
             "Despite being a seemingly sleepy rural community, what dark statistical running gag is frequently associated with the town of Brokenwood?: ",
             "What kind of classic car does Detective Inspector Mike Shepherd drive throughout the series?: ",
             "Who is Mike's young, multi-talented neighbor and local handyman who frequently helps him out and shares a relaxed, beer-drinking rapport?: ")

options = (("A. German coroner","B. Polish forensic psychologist","C. Ukrainian toxicologist","D. Russian pathologist"),
           ("A. Wayne Newton","B. Jhonny Cash","C. Glen Campbell","D. Willie Nelson"),
           ("A. It has the highest rate of vehicle thefts in the country", "B. It has the highest coffee consumpion per head", "C. It has an implausibly high murder rate per capita", "D. It suffers from a permanent water shortage crisis"),
           ("A. 1968 Ford Falcon", "B. 1971 Holden Kingswood" "C. 1956 Thunderbird", "D. 1965 Chrysler Valiant"),
           ("A. Kiri", "B. Ray Neilson", "C. Tim", "D. Jared Morehu"))

answers = ("D", "A", "C", "B", "D")
guesses = []
score = 0
question_num = 0

# breaks up the questions into there own parts and tells you if they are correct
for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess =input("Enter (A, B, C, D): ").upper() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

# shows you the results and score
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answer: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("answer: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")