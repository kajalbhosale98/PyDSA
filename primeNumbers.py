#print prime numbers between given range
def primeRange(n,m):
    for number in range(n, m + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)

print("The Prime Numbers in between given range are: ")
primeRange(1,100)

