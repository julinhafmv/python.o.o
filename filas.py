from typing import Deque, Any, Iterator
from collections import Deque

class Queue:
    """Uma classe representando uma fila"""

    def __innit__(self, maxlen=None) -> None:
        self.__items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items: Any) -> None:
        """Enqueue (enfileirar) é o mesmo que append"""
        for item in items:
            self.__items.append(item)

    def dequeue(self) -> Any:
        """Dequeue (desenfileirar) é o mesmo que popleft"""
        if not self:
            raise IndexError('pop from empty queue')

        return self.__items.popleft()

    def __repr__(self) -> str:
        return str(self.__items)

    def __bool__ (self) -> bool:
        return bool(self.__items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator:
        return sel.__items[index]

    def __getitem__(self, index: int) -> Any:
        return self.__items[items]

if __name__ == "__main__":
    fila = Queue()

fila. enqueue('A', 'B', 'C','D')

print(fila.__repr__())
print(fila.__getitem__(2))
print(fila.__bool__())
print(fila.__iter__())

fila.enqueue('D', 'E', 'F', 'G')

print (fila)

print('Item com índice 1:', fila[1], end = '/n/n')

for item in fila:
    print('Iteração:', item)
    

