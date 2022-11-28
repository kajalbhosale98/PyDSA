#find duplicate and missing number from list
def findDuplicateMissing():
    list1=[17,19,18,18,21]
    nonrep=[]
    low=min(list1)
    high=max(list1)
    DM=[]
    for i in list1:
        if i not in nonrep:
            nonrep.append(i)
        else:
            DM.append(i)
            break
    for j in range(low,high+1):
        if j not in nonrep:
            DM.append(j)
            break
    return DM

l=findDuplicateMissing()
print(l)

