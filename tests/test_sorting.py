import pytest  # noqa
import random
from algos import sorting


@pytest.fixture
def arrays():
    arr = [random.randint(0, 50) for _ in range(5)]
    return arr, sorted(arr)


def test_sort_selection(arrays, mock_renderer):
    arr, sorted_arr = arrays
    sorter = sorting.Selection(renderer=mock_renderer, speed=0)
    assert sorter.sort(arr) == sorted_arr


def test_sort_bubble(arrays, mock_renderer):
    arr, sorted_arr = arrays
    sorter = sorting.Bubble(renderer=mock_renderer, speed=0)
    assert sorter.sort(arr) == sorted_arr


def test_sort_insertion(arrays, mock_renderer):
    arr, sorted_arr = arrays
    sorter = sorting.Insertion(renderer=mock_renderer, speed=0)
    assert sorter.sort(arr) == sorted_arr
