tuple1 = ('a','b','c')
print(tuple1)

# now even if i don't write () while declaring the tuples it woul dbe same as this
tuple2 = 'a','b','c'
print(tuple2)

# But WE will always use () this was just to clarify that we can still see somewhere examples like these.


name='sagar'
age= 22
print(name, age,"python",2398)
print((name,age,"python",2398))
# this is anther way you can create a tuple
listFormTuple= list(tuple1)
print(listFormTuple)


print(len(tuple1))