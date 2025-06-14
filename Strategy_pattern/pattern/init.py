from typing import List
from .strategies import SortStrategy, BubbleSortStrategy

class Sorter:
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy or BubbleSortStrategy()
        # Ajoutez cette validation dans __init__
        if not isinstance(self._strategy, SortStrategy):
            raise ValueError("Strategy must be an instance of SortStrategy")

    def set_strategy(self, strategy: SortStrategy):
        if not isinstance(strategy, SortStrategy):
            raise ValueError("Strategy must be an instance of SortStrategy")
        self._strategy = strategy

    def perform_sort(self, data: List) -> List:
        if not isinstance(data, list):
            raise ValueError("Input data must be a list")
        return self._strategy.sort(data)