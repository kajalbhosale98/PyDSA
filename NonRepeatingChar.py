#print first non repeated character
string = 'ababb'
index = -1
res = ""
for i in string:
    if string.count(i) == 1:
        res += i
        break
    else:
        index += 1
if index == len(string)-1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is:-",res)
