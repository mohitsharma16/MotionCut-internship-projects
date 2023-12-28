def quiz():
    #Convert the 0 into a number so we can add scores
    score = 0 #initial score of the game is 0
    score = int(score)

    #user enter their name
    name = input("What is your name?")
    name = name.title()
    print("""
    Hello {}, welcome to Quiz night about HARRY POTTER! 
    You will be presented with 5 questions.
    Enter the option as(A,B,C,D) to answer the question
    Good luck!""".format(name))

    #Question1
    print("""Who was the Godfather of Harry Potter?
    A. Severus Snape                
    B. Serius Black
    C. Regulus Black
    D. None of the above""")

    answer1 = "B"
    response1 = input("Your answer is:").upper()

    if (response1 != answer1):
        print("Sorry, that is incorrect!" ,
          "The correct answer is"+ answer1)
    else:
        print("Well done! " + response1 + " is correct!")
    score = score + 1

    print("Your current score is " + str(score) + " out of 5")

    #Question2
    print("""What is the name of the Protagonist of the book series Harry Potter?
    A. Ronald Weasely
    B. Hermione Granger
    C. Nevile Longbottom
    D. Harry Potter""")

    answer2 = "D"
    response2 = input("Your answer is:").upper()

    if (response2 != answer2):
        print("Sorry, that is incorrect!",
          "The correct answer is"+ answer2)
    else:
        print("Well done! " + response2 + " is correct!")
        score = score + 1

    print("Your current score is " + str(score) + " out of 5")

    #Question3
    print("""What is the name of the Antagonist of the book series Harry Potter?
    A. Severus Snape 
    B. Bellatrix Lestrange
    C. Lord Voldemort
    D. Lucius Malfoy""")

    answer3 = "C"
    response3 = input("Your answer is:").upper()

    if (response3 != answer3):
        print("Sorry, that is incorrect!",
          "The correct answer is"+ answer3)
    else:
        print("Well done! " + response3 + " is correct!")
        score = score + 1

    print("Your current score is " + str(score) + " out of 5")

    #Question4
    print("""Who is the writer of the novel "Harry Potter"?
    A. J.K.Rowling  
    B. Charles Dickens
    C. Enid Bylton
    D. R.K.Mishra""")

    answer4 = "A"
    response4 = input("Your answer is:").upper()

    if (response4 != answer4):
        print("Sorry, that is incorrect!",
          "The correct answer is"+ answer4)
    else:
        print("Well done! " + response4 + " is correct!")
        score = score + 1

    print("Your current score is " + str(score) + " out of 5")

    #Question5
    print("""What is the real name of "Lord Voldemort"?
    A. Severus Snape
    B. Hagrid
    C. Tom Riddle
    D. Conilius Fudge""")

    answer5 = "C"
    response5 = input("Your answer is:").upper()

    if (response5 != answer5):
        print("Sorry, that is incorrect!",
          "The correct answer is"+ answer5)
    else:
        print("Well done! " + response5 + " is correct!")
        score = score + 1

    print("Your total score is " + str(score) + " out of 5")

    print("Thank you for playing {}, goodbye!".format(name))
    print("Do you want to play again Y/N")
    ans = input().upper()
    if (ans == "Y"):
        quiz()
    else:
        exit()
quiz()