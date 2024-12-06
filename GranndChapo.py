
def Max(A,O):
    if A<O:
        return O
    else:
        return A




# Your code here
A, O = [ int(e) for e in input().split()]
if A==0 or O==0:
    print(0)
else:
    print(Max(A,O))

