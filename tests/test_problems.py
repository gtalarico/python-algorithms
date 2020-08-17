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
def test_balanced_brackets(string, expected, mock_renderer):
    solver = problems.BalancedBracked(no_render=True, speed=0.001)
    assert solver.run(string) is expected
