class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self._list = [0] * self.capacity

    def get(self, i: int) -> int:
        return self._list[i]

    def set(self, i: int, n: int) -> None:
        self._list[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self._list[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self._list[self.length]

    def resize(self) -> None:
        self._list.extend([0] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity