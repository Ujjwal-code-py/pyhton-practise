li=[23,34,23,23,12]
li1=[i for i in range(6) if(i%2==0)]
print(li1)

class ujjwal:
    shirt="black shirt"
    def __init__(self,pant):
        self.pant=pant
        print('nice shirt')
bye=ujjwal("black trouser") #nice shirt is got printed it directly invoke the cunstructor #  self refer to  the  current object here bye is the current object

print(bye.pant)

class father:
    pant="white"
    child=ujjwal("BYE")
    print(child.pant)
trrouser=father()
print(trrouser.child)
        