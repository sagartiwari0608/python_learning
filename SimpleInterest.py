# # class SimpleInterestCal():
# #     def __init__(self,Principal,rate,time):
# #         self.Principal=Principal
# #         self.rate=rate
# #         self.time=time

# #     def SI(self,Principal,rate,time):
# #         simple=(Principal*time*rate)//100
# #         print(simple)

# # Principal = 100
# # rate = 2
# # time = 5
# # obj1 = SimpleInterestCal(Principal,rate,time)
# # obj1.SI(Principal,rate,time)
# tag=[]
# tag_rows,tag_cols=map(int, input().split())
# for i in range(tag_rows):
#     tag.append(list(map(int, input().split())))

# print(tag)
# for i in range(tag_rows):
#     arr=set(tag[i]) & set(tag[i+1])

# arr=sorted(arr)
# print



str=input()

def random(str):
    l1=[ord(e) for e in str]
    sum1 = sum(l1)
    return sum1/len(l1)
print(random(str))