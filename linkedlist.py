# linkedlist node creation
class _Node:
    __slots__ = "_element","_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next
n1=_Node(3,None)
