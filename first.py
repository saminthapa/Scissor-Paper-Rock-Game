import random
I=["rock","scissor","paper"]
while True:
    uc=int(input('''
    Game Start :--
    1 Play
    2 Exit
          '''))
    if uc==1:
        for a in range(1,4):
            userinput=int(input('''
            1 rock
            2 scissor
            3 paper
               '''))
            if userinput==1:
                userchoice="rock"
            elif userinput==2:
                userchoice="scissor"
            elif userinput==3:
                userchoice="paper"
                computerchoice=range.choice
                print(computerchoice)
                print(userchoice)





    else:
        break


if usercount==computercount:
    print("Your score :-",usercount)
    print("Computer score :-",computercount)
    print("Game Draw")
elif usercount>computercount:
    print("Your score :-",usercount)
    print("Computer score :-",computercount)
    print("You win")
else :
    print("Your score :-", usercount)
    print("Computer score :-", computercount)
    print("Computer win")



