data = [1,1,2,2,3,5,5,5,8,4,5,6,8,55,53,45,23,22]
print(data)
for index, value in enumerate(reversed(data)):
    print(index,value)
print(data)

# print(reversed(data))
# So we get to know from here that reversed just gives us the power to iterate in reverse order through an iterable without actually reversing the order of the iterable.
data2=reversed(data)
for i in data2:
    print(i)

data.reverse() # this thing would permanently change the order of list.

# lets test this with tuple as well.
nig= ("bruh","moment")
for i in reversed(nig):
    print(i)

# so this orks with tuple as well.
