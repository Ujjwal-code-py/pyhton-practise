
 
questions=[['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],
           ['Which language is used to build spotify','Python','JAVA','Php','Java script',2],]
levels=[1000,5000,10000,20000,50000,160000,320000,600000,2500000]
money=0

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for {levels[i]}\n{question[0]}")
    print(f"a.{question[1]}     b.{question[2]}\n"
          f"c.{question[3]}        d.{question[4]}")
    

 
    ans=int(input("Enter the ans(1-4) or You want to quit (0):"))
    if(ans==0):
        if(i==0):
            money=0
            break
        money=levels[i-1]
        break

    if(ans==question[5]):
        print(f"Sahi jawab aap jette hai {levels[i]}")
        if(i==2):
            money=10000
        elif(i==6):
            money=320000
    else:
        print("Afsos galat jawab")
        break
print(f"Aap jitte hai {money} rupees")


