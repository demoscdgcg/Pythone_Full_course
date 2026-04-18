
# variable only present inside function once function return there will no value in the variable
def sum(a,b):
    c=a+b
    return c



# global variable
z=34 # z is aglobal variable
print(sum(4,5))
print (z)


# local scope variable only present inside function once function return there will no value in the variable
def sum1(a,b):
    k=2
    c=a+b+k
    return c        
print(sum1(4,5))