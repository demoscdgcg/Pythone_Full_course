a=int(input("Enter the 1st no:"))
b=int(input("Enter the 1st no:"))

if b==0:
    raise ValueError("please donot devide by 0")

print(f"The division is{a/b}")    