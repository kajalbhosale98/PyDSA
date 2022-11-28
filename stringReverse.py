s="abcde"
res=''
i=0
while i<len(s):
    res=s[i]+res
    i=i+1
print(res)
#second Way
k="abcde"
res1=" "
for i in k:
    res1=i+res1
print(res1)
#thirdWay
print(s[::-1])