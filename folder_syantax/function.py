'''
a=4;
b=2;
c=1
avarage=(a+b+c)/3.0
print(avarage)
'''
# create a function it will start with def
# parameterised function
'''
def avarage(a,b,c):
    avarage=(a+b+c)/3.0
    return avarage  

print(avarage(4, 2, 1))
'''
# function with efault parameter
'''
def avarage(a,b,c=0):
    avarage=(a+b+c)/3.0
    return avarage  


print(avarage(4, 2))
print(avarage(4, 2, 1))
'''

# keyword argumets
'''
def avarage(a,b,c=0):
    avarage=(a+b+c)/3.0
    return avarage          


print(avarage(a=4, b=2))
print(avarage(a=4, b=2, c=1))
'''

# lamda function
'''
avarage=lambda a,b,c=0:(a+b+c)/3.0
print(avarage(4, 2))
print(avarage(4, 2, 1)) 
'''