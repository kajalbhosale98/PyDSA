# print the palindrome between given range
def countPal():
    count1 = 0
    for i in range(10, 1000):
        if str(i) == str(i)[::-1]:
            print(i)
            count1 += 1
    print("Total Count:-", count1)


countPal()
# cn=countPal()
# print("print count",cn)
