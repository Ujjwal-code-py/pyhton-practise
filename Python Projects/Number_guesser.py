import random
top_range=input("Type a number: ")
if(top_range.isdigit()):
    top_range=int(top_range)
    
    if(top_range<=0):
        print("Pleae type a range larger than 0 next time")
        quit()
else:
    print("Pleae type a number next time ")
    quit()

r = random.randrange(0,top_range) # if you want to choose no from range 0  to 10
guess=0
while True:
    guess+=1
    user_guess=input("Guess the no: ")
    if(user_guess.isdigit()):
        user_guess=int(user_guess)
    else:
        print("Pleae type a number next time ")
        continue

    if(user_guess==r):
        print("you got it")
        break
    elif(guess>(top_range/2)):
        print("Try next time")
        quit()
    
    elif(user_guess>r):
        print("You were above the no")
    else:
        print("You are below the no")
        
print("You got it in "+str(guess)+ " Guesses")
    
    
