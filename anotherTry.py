# # # # Your code here for lexicographical outputs

# # # S=input()
# # # print('hello')
# # # S=[str(i) for i in S]
# # # S.sort()
# # # print(S)
# # # op=''
# # # for i in range(len(S)):
# # #     op=op+ str(S[0])

# # # print(op)
# # # print('hello motherfucker;')


# # n= " My name is Vaibhav."
# # vowel=''
# # consonant=''
# # n.lower()
# # for j in n:
# #     if ord(j) in range(97,124):
        
# #         if j in ('a','e','i','o','u'):
# #             vowel+=j
# #         else:
# #             consonant+=j
# # print(vowel)
# # print(consonant)

# n="abskjnasds"
# print(set(n))
# n= sorted(n)
# print(n)
# for i in range(0,len(n)-2):
#     for j in range(i,len(n)-1):
#         if n[i]==n[j]:
#            print(n.pop(i+1))
#         else:
#             continue
# print(n)
# 


class Tree():
    def __init__(self,data):
        self.left= None
        self.right=None
        self.data=data

root= Tree(5)
root.left = Tree(3)
root.right= Tree(7)
root.left.left= Tree(1)
root.right.right = Tree(8)
print(root.right.data)


print("any number")
