# def cloth_washing():
#     detergent=5
#     water=2
#     no_clothes=int(input("How much kg clothes do you want to wash: "))
#     money=(no_clothes*water*detergent)
#     print("your payable amount is :",money)
#     return money
# print("Welcome to the laundry")
# cloth_washing()
        
    

    
    
# a=bool(input("do you want to add clothes(if )"))
# print(a)

# def sum(a=9,b=0):
#     sum=0
#     sum=a+b
#     return sum
# a=sum(15)
# print(a)



# P1
def area(b,h,shape):
    
    if(shape=="Triangle"):
        a = (1/2)*b*h
        print("area of trianle is ",a)
        return a
    elif(shape=="Rectangle"):
        a=length*width
        print("Area of rectangle is ",a)
        return a
    else:
        pass
area(4,5,"Triangle")

# p2

def pattern_print(n):
    a=""
    for i in range(n):
        a+="*"
        print(a)
    
pattern_print(5)

def password_strength(password):
    """funtion is for checking the password strength"""
    if(len(password)<8):
        print("Create a password of length 8")
        return False
    elif not any(char.isdigit() for char in password):
        print("add a digit in your password")
        return False
    elif not any(char.islower() for char in password):
        print("Add a lower case charecter in your password")
        return False 
    elif not any(char.isupper() for char in password):
        print("Add a Upper  case charecter in your password")
        return False 
    elif not any(char in '!@#$%&*' for char in password):
        print("Add a symbol   charecter in your password")
        return False  
    else:
        
        return True
print(password_strength("weakpass"))
print(password_strength("E#3eakpass"))


