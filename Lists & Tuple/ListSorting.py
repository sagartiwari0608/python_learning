odd = [1,3,5,7,9]
even = [2,4,6,8,0]

# even.append(odd)        # this method will append the second list as it is adn give [2,4,6,8,0,[1,3,5,7,9]] 

even.extend(odd)          # this will take the items and append one by one [2,4,6,8,0,1,3,5,7,9] we will get this as ooutput
print(even)

odd=even.copy()        # I had to use copy here because otherwise python was using same list and odd was getting sorted too.
even.sort()       #for sorting the list and it will make changes to original list soo we dont need to store it anywhere else

print("even",even)

nigga=sorted(odd)
print("nigga", sorted(odd))
print("odd",odd)

even.sort(reverse=True)
# now this will reverse the shit
print(even)

all_list=[1,2,3,4,5,6,7,8,9]           
print(all_list)                 #this method is used to check if all the items are iterable in an iterable or not. means al items are true or not 
print(all(all_list))
all_list1=[1,2,3,4,5,6,7,8,9,0]
print(all_list1)                # at first it gave us ture because there was no zero as soon as we added one zero we got false.
print(all(all_list1))


# Python can sort  strings too but it will have to be by using sorted() method
Pangram = "The quick brown fox jumps over a lazy dog."  # pangrams are those phrases which contain all the enligsh alphabets.
sorted_pangram = sorted(Pangram)        # Also this sorted method takes whatever is written in it and treats as a stirng list. so output is also list of sorted strings    
print(sorted_pangram)                   # This was a case sensitive sorting. thats why we got Capital T before everyone else.

# now lets try one which is not sensitive to cases.
Pangram2 = "The quick brown fox jumps over a lazy dog."
sorted_pangram2 = sorted(Pangram2,key=str.casefold) 
print(sorted_pangram2)

# Now the output is as expected.

Names = ["sagar","tmatar","gandhi","Jaggi"]
Names.sort(key=str.casefold)
print(Names)