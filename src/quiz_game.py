print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play! :)")

points = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! Nice job!")
    points += 1
else:
    print("Incorrect!")
####################################################
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! Nice job!")
    points += 1
else:
    print("Incorrect!")
####################################################
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! Nice job!")
    points += 1
else:
    print("Incorrect!")
####################################################
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct! Nice job!")
    points += 1
else:
    print("Incorrect!")

if points == 0:
    print("You scored " + points + "points! Time to study!")
elif points == 1:
    print("You scored " + points + "points! That's only 25% :(")
elif points == 2:
    print("You scored " + points + "points! Eh, you could do better!")
elif points == 3:
    print("You scored " + points + "points! Only one answer from perfect!")
else:
    print("You scored " + points + "points! You're amazing! 100%!")    
