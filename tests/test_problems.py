import pytest  # noqa
from algos import problems


@pytest.mark.parametrize(
    "string, expected",
    [
        ("[]", True),
        ("[{()}]", True),
        ("()()", True),
        ("()[]", True),
        ("(]", False),
        ("]", False),
        ("(", False),
        ("([)]", False),
    ],
)
def test_balanced_brackets(string, expected):
    solver = problems.BalancedBracked(render=False)
    assert solver.sort(string) is expected
