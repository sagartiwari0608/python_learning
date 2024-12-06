# # # def count_numbers(k, n, flag) :
 
# # #     # Base case
# # #     if (n == 1) :
 
# # #         # If 0 wasn't chosen previously
# # #         if (flag) :
# # #             return (k - 1)
# # #         else :
# # #             return 1
 
# # #     # If 0 wasn't chosen previously
# # #     if (flag) :
# # #         return (k - 1) * (count_numbers(k, n - 1, 0) +
# # #                           count_numbers(k, n - 1, 1))
# # #     else :
# # #         return count_numbers(k, n - 1, 1)
 
# # # # Driver code
# # # n,k=input().split()
# # # n=int(n)
# # # k=int(k)
# # # print(count_numbers(k, n, True))







# # from re import X



# # N = int(input())
# # for i in range(N):
# #     hours , extra = [float(e) for e in input().split()]
# #     hours=int(hours)
# #     output = (hours*20) + (extra*(hours-40))
# #     print(output)


# # def Check_Vow(string_inp, vowels):
# #     count_a= string_inp.count('a')
# #     count_e= string_inp.count('e')
# #     count_i= string_inp.count('i')
# #     count_o= string_inp.count('o')
# #     count_= string_inp.count('u')
# #     max=0
# #     for i in range(5):
# #         if count_
    
# # vowels = 'aeiou'
# # string_inp = input().casefold()
# # print (Check_Vow(string_inp, vowels))



# # Count vowels in a different way
# # Using dictionary




# def Check_Vow(string, vowels):
     
#     string = string.casefold()
     
#     count = {}.fromkeys(vowels, 0)
     
#     for character in string:
#         if character in count:
#             count[character] += 1   
#     return count
     
# vowels = 'aeiou'
# N= int(input())
# string = input()
# if len(string) == N:
#     count2=Check_Vow(string, vowels)
#     max_count_vowel=max(count2,key= count2.get)
#     print(max_count_vowel)
arr = [1,2,3,4,5,6,7]
d=3
for i in range(3):
    temp= arr.pop()
    print(temp)
    arr.append(temp)
print(arr)

