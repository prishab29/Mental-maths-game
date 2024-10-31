import random
a = (int(input("Choose an operation to practice:\nAddition'1'\nSubtraction'2'\nMultiplication'3'\nDivision'4'\nYour choice: ")))
#This is for the code to take in the users choice of operation
b = (int(input("Choose a difficulty level:\nEasy'1'\nMedium'2'\nHard'3'\nYour choice: ")))
#This is for the code to take in the users choice of level of difficiutly
score = 0
#This is for the user to see their score out of 20 at the end
score = 0
if b == 1:  # Easy
    r = range(0, 20)
elif b == 2:  # Medium
    r = range(0, 50)
else:  # Hard
#These are the ranges for different difficulty levels
        num_range = range(0, 100)
if a == 1 and b == 1:
#This is for when the user chooses addition and level easy
    for i in range(1, 20):
    #Range is used so that there are 20 questions
        #These are the random generated numbers for the questions
        d= random.choice(r)
        e= random.choice(r)
        a1= (int(input(f"q{i}){d}+{e}: ")))
        correcta = d+e
        if a1 == correcta:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
             #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d+e)
elif a==1 and b==2:
    for o in range (1, 20):
    #Range is used so that there are 20 questions
    #These are the random generated numbers for the questions
        d= random.choice(r)
        e= random.choice(r)
        a2= (int(input(f"q{o}){d}+{e}: ")))
        correcta = d+e
        if a2 == correcta:
            print ("Correct ✔")
            #This is what the code outputs if the users answer is correct
            score += 1
            #This is so they can see their score at the end
        else:
             #This is what the code outputs if the users answer is wrong
            print ("Wrong ✘, Correct answer is:",d+e)
        