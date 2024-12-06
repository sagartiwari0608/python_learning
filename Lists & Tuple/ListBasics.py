# List is a python data type similar to arrays.
#  I said similar because arrays are only capable to store homogenous datatype.
#  but list are just intended to be homogeneous and all of list functions are meant for homogeneous items. like sort join etc.
# how ever there will not be a error if we try to store differet types . we will get errors if we try to use inbuilt functions.


digits = list("163,450,6543,213".split(",")) # this .split() function defines where to split and if we dont specify then it will split in one by one pieces .
print(digits)

#  Or if i do this 
digits1 = sorted("1634506543213")
print(digits1)

another_digits = list(digits1)
print(another_digits)
# the output for this and above will be same 

# now here we will check if theese two lists are just using one single refference or they are different.
print(id(another_digits))
print(id(digits1))
# here we got Different id's so these are copy of each other. and these are 2 lists.
#if these two arre same then they are same reference otherwise these are just copy of each other 

# WE have other methodsa to check as well
print(another_digits is digits1)    # False (this "is" operator checks if both are single reference or not is they are then ture false otherwise)

# and 

print( another_digits == digits1)       # True ( because the values inside them are same so this == will give us true resuilt means that yes these two l;ists are same)

# So we hav eseen a way to copy a list. now there are other methods as well.

# SLICING
digits1_copy = digits1[:]  #this will copy all the list from starting to end usually the slice [start : end : gap] has three parts start,end and jump distances or gap.
# if we dont mention any of these then start will be start of list and end will be end of list and gap will be of 1. by default and end is not inculded because length is always -1 the actual length.

#   USING .COPY()
digits1_copy2 = digits1.copy()



available_parts1 = ["computer", "monitor","keyboard","mouse","hdmi cable","Dvd Drive"]
available_parts1[1:3]= [88687]
print(available_parts1)
# when we replaced with "Niggers" we got n i g g e r s in place of monitor keyboard.

# now we can also just delete the items from the list.

data=[1,2,3,4,5,65,67,78,0,-45,6,7,8,7]

# del data[2:5]
print(data)

# since this method deletes the slice so we have to remember  that the size of the list also changes and positions of the items also changes.
# Now lets say we dont want to do it maually we want it to so it through loop.
# for index,item in enumerate(data):
#     if item>10 or item <0:
#         del data[index]
#         index-=1
# print(data)

# since we already saw that this wont work reason is that enumerate function will reset the value of index to whatever the item it is currently on.

# so we will see other methods.
# in other methods what we do is we just first sort the list and then remove the items. 
data.sort()
min_value=1
max_value=10
stop=0          # we are using word stop because we are deleting the item from start so we will be finding the number where to stop.
for index,item in enumerate(data):
    if item>=min_value:
        stop= index
        break
print(stop)
del data[:stop]
print(data)

# Now we start from end for removing the items and we will find the last item to keep in the list.
# remember one more thing that deletion of slice always happends from left to right.
# if we are deleting one by one then we can start from the end and go till start.
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_value:
        start = index+1 # because the value we got is last to keep so the item from next and onwards will be deleted.
        break
print(start)
del data[start:]
print(data)

# Now we got the correct output.
data1=[1,2,3,4,5,65,67,78,0,-45,6,7,8,7]
min_value=1
max_value=10
for index in range(len(data1)-1,-1,-1):
    if data1[index]>max_value or data1[index]<min_value:
        print(index,data1)
        del data1[index]

print(data1)

# now why did this work because items get deleted one by one.
# now that we have seen all the ways ti delete but the best way to do is the 
# first where we find out the number of items to delete and number of items to keep
# because we just delete the items 2 times and then python rearranges the items in the list.
# and in other ways python rearranges the items every time it deleted the items and items are being delted one by one.

