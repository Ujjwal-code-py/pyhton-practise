import random
user_wins=0
computer_wins=0
option=["rock","paper","scissor"]
while True:
    user=input("What do you want Rock,Paper,Scissor or Q for Quit: ").lower
    if(user=="q"):
        break
    if user not in option:
        continue
    random_no=random.randint(0,2)
    # rock 0
    # paper 1
    # scissor 2
    computer_pick=option[random_no]
    print("compter picked",computer_pick,+".")
    if(user=="rock" and computer_pick=="scissor"):
        print("you won")
        user_wins+=1
        continue

    if(user=="rock" and computer_pick=="paper"):
        computer_wins+=1
        print("You loose")
        continue
    if(user=="paper" and computer_pick=="scissor"):
        computer_wins+=1
        print("You loose")
    if(user=="paper" and computer_pick=="rock"):
        user_wins+=1
        print("You win")
    if(user=="scissor" and computer_pick=="paper"):
        user_wins+=1
        print("You win")
    
print("good bye!")
     

    