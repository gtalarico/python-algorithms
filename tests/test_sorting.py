import pytest  # noqa
import random
from algos import sorting


@pytest.fixture
def arrays():
    arr = [random.randint(0, 100) for _ in range(100)]
    return arr, sorted(arr)


def test_sort_selection(arrays):
    arr, sorted_arr = arrays
    sorter = sorting.Selection(render=False)
    assert sorter.sort(arr) == sorted_arr


def test_sort_bubble(arrays):
    arr, sorted_arr = arrays
    sorter = sorting.Bubble(render=False)
    assert sorter.sort(arr) == sorted_arr
