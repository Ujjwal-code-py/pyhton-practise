list=[2,4,5,6,3,2]
# agar tujhe uska index or element chahiye to kya karega for loop use simple wala

# old way to do this
# index=0
# for pt in list:
#     print(pt)
#     if(index==3):
#         print('bye')
#     index+=1


# use enumerete function directly to get index and value from list tuple (index, mark)


# for index,mark in enumerate(list):
#     print(mark)
#     if(index==3):
#         print('hello hello')
        
# you also assign the startin index
for index,mark in enumerate(list,start=1):
    print(mark)
    if(index==3):
        print('hello hello')
        