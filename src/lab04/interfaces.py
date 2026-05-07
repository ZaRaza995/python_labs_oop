from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые могут выводить информацию о себе."""
    
    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта."""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать между собой."""
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
        -1, если self < other
         0, если self == other
         1, если self > other
        """
        pass
