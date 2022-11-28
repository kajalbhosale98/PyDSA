'''n=1
while n<21:
    print(n)
    if n%3==0 and n%5==0:
        break
    n=n+1
print("Devide by 3 and 5")

i=1
while i<101:
    print(i)
    if i==50:
        break
    i=i+1
print("Executed Till 50")
#####################   Fstring
arr=[4,20,30,40]
for i,v in enumerate(arr):
    print("index is",i,"value is",v**2)
    print("index is {} and value is {}".format(i,v**2))
    print(f"index is {i} and value is {v**2}")

d={1:'abc',2:"pqr",3:"xyz",4:"xpr"}
for key,value in d.items():
    print("key is ",key,"value is","'",value,"'")
for key,value in d.items():
    print(f"key is {key} and value is ' {value} ' ")

def func():
    return 10,20,30
x,y,z=func()
print(x)
'''


def oddList(n):
    for i in range(n):
        if i % 2 != 0:
            l1.append(i)
    return l1


l1 = []
n = int(input())
print(oddList(n))
