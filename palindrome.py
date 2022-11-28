# print the palindrome between given range
def countPal():
    count = 0
    for i in range(10, 1000):
        if str(i) == str(i)[::-1]:
            print(i)
            count += 1
    print("Total Count:-", count)


countPal()
# cn=countPal()
# print("print count",cn)
