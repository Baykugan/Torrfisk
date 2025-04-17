import numba as nb


@nb.vectorize(
    [
        nb.i8(nb.u8),
        nb.i8(nb.i8),
    ],
    cache=True,
)
def popcount(n):
    """Returns the number of set bits (Hamming weight) in an integer n."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
