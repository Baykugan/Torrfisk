import numpy as np
import pytest

from torrfisk.utils import popcount


@pytest.mark.parametrize(
    "input, expected",
    [
        # 0d array inputs
        (0, 0),
        (np.uint8(5), np.uint8(2)),
        # 1d array inputs
        ([0, 1, 3, 255], [0, 1, 2, 8]),
        (np.array([7, 8, 15], dtype=np.uint8), np.array([3, 1, 4])),
        # 2d array inputs
        ([[0, 1], [2, 3]], [[0, 1], [1, 2]]),
        (np.array([[15, 16], [31, 32]], dtype=np.uint64), np.array([[4, 1], [5, 1]])),
        # Edge cases
        (np.array([], dtype=np.uint8), np.array([], dtype=np.uint8)),
    ],
)
def test_popcount(input, expected):
    """Test the popcount function."""
    result = popcount(input)
    assert np.array_equal(result, expected), f"Expected {expected}, got {result}"
