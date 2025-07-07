print('WELCOME TO THE QUIZ GAME!')
playing= str.lower(input("Do you want to play this game (yes/no)? "))
if(playing != "yes" and playing != "y"):
    
    quit()

Score=0
    
print("OK! lets Play :) ")
ans=str.lower(input("What does Cpu stand for? "))
if(ans=="central processing unit"):
    print("correct")
    Score += 1
else:
    print("incorrect ")
    

ans=str.lower(input("What does gpu stand for? "))

if(ans=="graphical processing unit"):
    print("correct")
    Score += 1
else:
    print("incorrect")
    
    
ans=str.lower(input("What does RAM stand for? "))
if(ans=="random access memory"):
    print("correct")
    Score += 1
else:
    print("correct ")
    
    
print("You got "+str(Score)+ " questions correct!")
print("You got "+str(((Score/3) * 100) )+ "%.")