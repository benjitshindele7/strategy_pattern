from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List) -> List:
        data = data.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSortStrategy(SortStrategy):
    def sort(self, data: List) -> List:
        if len(data) <= 1:
            return data.copy()
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class ReverseSortStrategy(SortStrategy):
    def sort(self, data: List) -> List:
        return sorted(data, reverse=True)