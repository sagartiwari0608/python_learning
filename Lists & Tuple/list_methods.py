# "separator".join(iterable) tis iterates the whole thing and combines the items with the "separator" in between them
# separator can be empty too.
# it will all happen and be temporary to make it pernmanent will have to store it in a variable or print it out.

# " seperator ".join(iterable) this function is used for joining the items of th elist with the defined separator.
# just for that pupose this nigga is used.

generated_list = ['1','2','3','4','5','6']
burh = "_".join(generated_list)
print(burh)



l1= ["nigga","nigger","nigg"]
print("brih ".join(l1))
print(l1)

# iterable.split("separator") method is used to create a list .
pangram = "bruh moment is  necessary"
words1 = pangram.split()
words2 = pangram.split("is")
print(words1)
print(words2)
print(type(words1))

# join will let us create astring from a sequence, such as a list split. Split,on the other hand will let us create list from string by splitiing it in desired parts and positions.
l2 = ['9','223','372','335']
for i in range(0,len(l2)):
    l2[i]=int(l2[i])

# # OR
# intt_list =[]
# for value in l2:
#     intt_list.append(int(value))

print(l2)


# If we use triple quotation marks then we can save the format of the string. whatever we write it will oprint out the same.
try1="""bruh moment
is something that we \t want """
try2="i dont know \n something random"
print(try2)
print(try1)
