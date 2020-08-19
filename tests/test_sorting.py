import pytest  # noqa
import random
from algos import sorting


@pytest.fixture
def arrays():
    arr = [random.randint(0, 50) for _ in range(10)]
    return arr, sorted(arr)


@pytest.mark.parametrize(
    "SortCls", [sorting.Bubble, sorting.Selection, sorting.Insertion, sorting.MergeSort]
)
def test_sort(SortCls, arrays, mock_renderer):
    arr, sorted_arr = arrays
    sorter = SortCls(renderer=mock_renderer, speed=0)
    assert sorter.sort(arr) == sorted_arr
