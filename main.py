#This is a scissor paper rock game
import random
choice=['s','p','r']
while True:
    user=input("enter you preferred choice(s for scissor,p for papper, and r for rock)")
    computer=random.choice(choice)
    if (computer=='s'):
        print("Computer choice was 'SCISSOR'")
        if (user=='p'):
            print("you lose")
        if (user=='r'):
            print("you won")
        if (user=='s'):
            print("its a tie")
    if (computer=='p'):
        print("Computer choice was 'PAPER'")
        if (user=='r'):
            print("your lose")
        if (user=='s'):
            print("you won")
        if (user=='p'):
            print("its a tie")
    if (computer=='r'):
        print("Computer choice was 'ROCK'")
        if (user=='s'):
            print("you lose")
        if (user=='p'):
            print("you won")
        if (user=='r'):
            print("its a tie")
    p=input("press 'q' to quit , press enter to continue" )
    if(p=='q'):
        break


        

    


