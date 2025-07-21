import random

moves=["rock","paper","scissors"]
print("------- ROCK PAPER SCISSORS -------")
print()
while True:
    computer_choice=random.choice(moves)
    print("PRESS 1 FOR ROCK")
    print("PRINT 2 FOR PAPER")
    print("PRINT 3 FOR SCISSORS")
    user_input=input("Enter your move (1/2/3):")

    if(user_input=="1" and computer_choice=="scissors") or (user_input=="2" and computer_choice=="rock") or (user_input=="3" and computer_choice=="paper"):
        print("CONGRATULATIONS!! YOU WIN THE GAME")
    elif(user_input=="2" and computer_choice=="scissors") or (user_input=="3" and computer_choice=="rock") or (user_input=="1" and computer_choice=="paper"):
        print("OOPS!! THE COMPUTER WINS THE GAME")
    elif(user_input=="3" and computer_choice=="scissors") or (user_input=="1" and computer_choice=="rock") or (user_input=="2" and computer_choice=="paper"):
        print("WHOA!! IT'S A TIE")
    else:
        print("This is an invalid choice")
    print("THE GAME IS OVER")

    #TO CONTINUE THE GAME
    ask=input("Do you want to play again? {yes/no}")
    if ask not in["yes"]:
        break
