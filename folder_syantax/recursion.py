# febanic series
def feba():
    a=0
    b=1
    n=int(input("Enter the number of terms : "))
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c     
# return feba()

print(feba())