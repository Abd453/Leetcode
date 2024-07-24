class MyLinkedList:

    def __init__(self):
        self._storage = []
        
    def get(self, index: int) -> int:
        if index > len(self._storage) - 1:
            return -1
        
        return self._storage[index]
        
    def addAtHead(self, val: int) -> None:
        self._storage.insert(0, val)
        
    def addAtTail(self, val: int) -> None:
        self._storage.append(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self._storage):
            self._storage.insert(index, val)
        elif index == len(self._storage):
            self._storage.append(val)
        
    def deleteAtIndex(self, index: int) -> None:
        if index > len(self._storage) - 1:
            return
        
        self._storage.pop(index)