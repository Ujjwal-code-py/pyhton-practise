import random
char='abcdefghijklmnopqrstuvwxyz'

encoded=''
def coding(word='helo'):
    if(len(word)<=3):
        
        global encoded
        
        encoded += word[1:]
        encoded+=word[0]
        random_chS=random.sample(char,3)
        random_chS=str(random_chS)
        print(random_chS)
        
    print(encoded)
coding(word='yel')
# def decode():
    
    