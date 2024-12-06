n="abskjnasds"

list1=sorted(n)
print(set(list1))

# list1= [1,2,3,4,1,3,4]
# list1.sort()
for i in range(0,len(list1)-2):
    for j in range(i,len(list1)-1):
        if list1[i]==list1[j]:
            list1.pop(i+1)

print(list1)
print(set(list1))

# a string of pearls with n pearls 2 persons 
# no of pearls 

# l1=[]
# l2=[]
# n = 7
# for i in range(1,n):
      
#     if n%2 ==1 or n%3==1:
#         print(i)
#         print(n%i)
#     if n%i==0:
#         print(i)    
       
# print("possible number of pearls" , )
# print(" possible number of persons", )