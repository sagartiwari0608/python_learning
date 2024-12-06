empty_list = []
even = [2,4,6,8,0]
odd = [1,3,5,7,9]

number1 = even + odd
number2 = [even + odd]
number3 = [even,odd]
print(number1)
print(number2)
print(number3)
for numbers_list in number3:
    print(numbers_list)
    for items in numbers_list:
        print(items)