# here we are making just a shopping list where we can add items to our list and remove items from out list

available_parts = ["computer", "monitor","keyboard","mouse","hdmi cable","Dvd Drive"]

valid_choices = []  #created an empty list
for i in range(1,len(available_parts)+1):
    valid_choices.append(str(i))

print("your valid choices are: {}".format(valid_choices))

current_choice = "Something"    #we have initialised it to just anything random
parts_to_buy = []
while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice)-1                   # because list and array index starts from 0 thats why all positions will be -1
        chosen_part = available_parts[index]
        if chosen_part in parts_to_buy:
            print("Removing {}".format(current_choice))
            parts_to_buy.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            parts_to_buy.append(chosen_part)                # Here we are adding the item but what if someone adds wrong part by mistake. thatswhy we made this condition and option to remove person can remove just by clicking same number twice.


    else:
        print("Please add options from the list below: ")

        for number, part in enumerate(available_parts):     # enumerate is a python function which gives us the ability to iterate through an iterable and gives us index of the item as well 
            print("{}:{}".format( number+1, part))          # This can also be done manually but it would be an additional step and too ime consuming in real time. so we use enumerate

    current_choice = input()

print("your selected items are :",parts_to_buy)