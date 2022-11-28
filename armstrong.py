
def armstrongCheck(n):
    b=len(str(n))
    sum1=0
    s=n
    while n != 0:
        r = n % 10
        sum1 = sum1+(r**b)
        n = n//10
    return (s==sum1)
    '''if s == sum1:
        print(f"The given number {s} is armstrong number")
    else:
        print(f"The given number {s} is not armstrong number")'''

n=int(input("Enter any number:"))
print(armstrongCheck(n))
