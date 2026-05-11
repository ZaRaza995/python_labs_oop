from typing import TypeVar, Generic, Callable, Optional, Protocol
class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить в виде строки."""
    def display(self) -> str:
        ...

class Billable(Protocol):
    """Протокол для объектов, которым можно выставить счет."""
    def get_bill_amount(self) -> float:
        ...

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
B = TypeVar('B', bound=Billable)


class TypedCollection(Generic[T]):
    """Строго типизированная коллекция."""
    
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)


    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый подходящий элемент или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Возвращает список всех подходящих элементов."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Применяет функцию ко всем элементам, меняя тип результата (R)."""
        return [transform(item) for item in self._items]
