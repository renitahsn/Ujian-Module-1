# def Hastag(string):
#     word = str(string)
#     a = ''
#     b = a.join(word)
#     if len(string)>140:
#         return False
#     elif len(string)==0:
#         return False
#     # a.join(word)
#     # for item in string:
#     #     word.join(item)
#     print('#{}'.format(b.capitalize()))
    
# Hastag("Hello there how are you doing")
    

# # No 2
# def create_phone_number(number):
#     for i in number:
#         print(i,end='')
    
 
# create_phone_number([1,2,3,4,5,6,7,8,9,0])
   


# NO 3
# def sort_odd_even(num):
#     ganjil = []
#     genap = []

#     for i in num:
#         if i%2==1:
#             ganjil.append(i)
#         else:
#             genap.append(i)

#     for i in range(len(ganjil)):
#         for j in range(i+1, len(ganjil)):
#             if ganjil[i] > ganjil[j]:
#                 ganjil[i], ganjil[j] = ganjil[j], ganjil[i]
#     return ganjil

#     for i in range(len(genap)):
#         for j in range(i+1, len(genap)):
#             if genap[i] < genap[j]:
#                 genap[i], genap[j] = genap[j], genap[i]
#     return genap

#     print(ganjil.append(genap))

# sort_odd_even([5,3,2,8,1,4])

#No 4
# def hollowTriangle(num):
#     k = ''
#     for row in range(1,num+1):
#         for col in range(1,2*num):
#             if row+col==num+1 or col-row==num-1:
#                 print(" # ",end="")
#                 if row==num and col!=num:
#                     print(" _ ",end="")
#                     k= num
#             else:
#                 print(end=" ")
#         print(k)
# hollowTriangle(4)



