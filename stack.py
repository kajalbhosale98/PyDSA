class StackArray:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data)==0

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.isempty():
            print("Stack is empty")
        return self._data[-1]

ob1 = StackArray()
ob1.push(5)
ob1.push(6)
print(ob1._data)
print(len(ob1))
ob1.push(9)
print(len(ob1))
ob1.pop()
ob1.pop()
ob1.pop()
print(ob1.isempty())
ob1.push(8)
ob1.push(2)
print(ob1.top())
print(ob1._data)








'''class StacksArray:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data[-1]


S = StacksArray()
S.push(5)
S.push(3)
print(S._data)
print(len(S))
print(S.pop())
print(S.isempty())
print(S.pop())
print(S.isempty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
S.push(8)
print(S.pop())
'''



