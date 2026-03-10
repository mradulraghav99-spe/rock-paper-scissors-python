'''
Rock Paper Scissors – Best of 5

'''



import random

player_score=0
computer_score=0

while player_score<3 and computer_score<3:
    computer=random.choice([1,0,-1])

    youinp=input("Enter your choice 'r' for rock 's' for scissor and 'p' for paper:")

    dictyou={'r':1,'p':0,'s':-1}
    chosedict={1:'Rock',0:'Paper',-1:'Scissor'}

    if youinp  not in dictyou:
        print("Something is wrong!")
        continue


    you=dictyou[youinp]

    print(f"You chose {chosedict[you]}\n Computer chose {chosedict[computer]}")
    
    

    if(computer==you):
        print("It's a draw!")
    else:
        if(computer==1 and you==-1 or computer==0 and you==1 or computer==-1 and you==0):
            print("you lose!")
            computer_score+=1
        elif(computer==-1 and you==1 or computer==1 and you==0 or computer==0 and you==-1):
            print("you won")   
            player_score+=1
        
        
    print(f"Your score {player_score}\n Computer score {computer_score}")

    

if(player_score==3):
        print("🎉 You won the match!")
else:
     print("💻 Computer won the match!")    

    