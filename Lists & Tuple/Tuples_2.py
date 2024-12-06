a=b=c=e=d=f=29
print(c)
# this will print 29
f=15
print(d)
# this will print 29 as well only f will print 15

# now if we remeber using this format to "UNPACK "
print("Unpacking tuple")

x,y,z=1,2,45
print(x)
print(y)
print(z)
# here if we see on the right side or = 1,2,45 is a tuple.
# same can be done with list too .
print("unpacking list")
x,y,z=[1,2,45]
print(x)
print(y)
print(z)

# now if we see the function ENUMERATE(list or tuple) 
for index , item in enumerate("abcedefgijklmnop"):
    print(index,item)

for t in enumerate("abcedefgijklmnop"):
    print(t)

# here we can conclude that this enumerate returns a tuple of (index, value) which we were unpacking in without even knowing.

albums=[("welcome home","random1",2929),
("bad Company","random2",2828),
("Night Life","ranom 3",2020)]
print(len(albums))
for album in albums:
    name,artist,year=album
    print( "Album:{}, Artist:{}, Year:{}" .format(name,artist,year))
