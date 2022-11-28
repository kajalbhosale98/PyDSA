#sort list by using one for loop
def sortArray(s):
    sortedList=[]
    for i in range(len(s)):
        a=min(s)
        sortedList.append(a)
        s.remove(a)
    return sortedList

s=[0,1,0,1,-1,0,-1,-1]
res=sortArray(s)
print("Sorted list is:",res)

#b = input()
a = list(map(int, b[1:(len(b) - 1)].split(",")))

i = 0
while (i < len(a)):

    def data(ap):
        if (a[i] > a[ap]):
            a[i], a[ap] = a[ap], a[i]
        if (ap == len(a) - 1):
            pass
        else:
            ap = ap + 1
            data(ap)


    data(i)
    i = i + 1
print(a)