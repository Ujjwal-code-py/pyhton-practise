import json
person={}
person['ujjwal']={
    'name':"ujjwal",
    'Education':"Persuing Engineering"
}
person['hitesh']={
    'name':"hitesh",
    'Education':"Persuing Engineering"
}



s=json.dumps(person)
print(s)
with open("hello//file.txt","w+") as f:
    f.write(s)
# a=json.loads(s) // it is used to convert json in to string in to dictionary format
# print(a)
    
# f=open("hello//bin.txt","w+")
# f.write("i am chubby")
# f.close()
# s=open("hello//bin.txt","r")
# p=s.read()
# print(p)

# s.close()

