import pytest
import sys
import os
from unittest.mock import MagicMock

# Ajoute le chemin du projet au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'test.env')))
import pytest
from unittest.mock import MagicMock
from pattern.context import Sorter
from pattern.strategies import (
    BubbleSortStrategy,
    QuickSortStrategy,
    ReverseSortStrategy,
    SortStrategy
)
class TestStrategyPattern:
    @pytest.fixture
    def test_data(self):
        return [5, 2, 8, 1, 9]

    @pytest.fixture
    def sorted_asc(self):
        return [1, 2, 5, 8, 9]

    @pytest.fixture
    def sorted_desc(self):
        return [9, 8, 5, 2, 1]

    # Tests positifs
    def test_bubble_sort(self, test_data, sorted_asc):
        sorter = Sorter(BubbleSortStrategy())
        assert sorter.perform_sort(test_data) == sorted_asc

    def test_quick_sort(self, test_data, sorted_asc):
        sorter = Sorter(QuickSortStrategy())
        assert sorter.perform_sort(test_data) == sorted_asc

    def test_reverse_sort(self, test_data, sorted_desc):
        sorter = Sorter(ReverseSortStrategy())
        assert sorter.perform_sort(test_data) == sorted_desc

    def test_change_strategy(self, test_data, sorted_asc, sorted_desc):
        sorter = Sorter(BubbleSortStrategy())
        assert sorter.perform_sort(test_data) == sorted_asc
        
        sorter.set_strategy(ReverseSortStrategy())
        assert sorter.perform_sort(test_data) == sorted_desc

    # Tests négatifs
    def test_invalid_strategy(self):
        with pytest.raises(ValueError):
            Sorter("not a strategy")

    def test_invalid_data_type(self, test_data):
        sorter = Sorter(BubbleSortStrategy())
        with pytest.raises(ValueError):
            sorter.perform_sort("not a list")

    # Test avec mock
    def test_mock_strategy(self, test_data):
        mock_strategy = MagicMock(spec=SortStrategy)
        mock_strategy.sort.return_value = [1, 2, 3]
        
        sorter = Sorter(mock_strategy)
        result = sorter.perform_sort(test_data)
        
        mock_strategy.sort.assert_called_once_with(test_data)
        assert result == [1, 2, 3]

    def test_mock_strategy_exception(self, test_data):
        mock_strategy = MagicMock(spec=SortStrategy)
        mock_strategy.sort.side_effect = Exception("Sort error")
        
        sorter = Sorter(mock_strategy)
        
        with pytest.raises(Exception):
            sorter.perform_sort(test_data)