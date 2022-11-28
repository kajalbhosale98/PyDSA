n=int(input("Enter number:"))
flag=0
i=2
while i<n:
    if n % i == 0:
        flag=1
        print(i)#printing factors
    i=i+1

if flag==0:
    print(n,"is prime number.")
else:
    print(n,"is not prime number.")