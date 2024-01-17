import pytest
from Task4 import fibonachi

def testFibonachi():
    assert fibonachi(1) == 0
    assert fibonachi(2) == 1
    assert fibonachi(3) == 1
    assert fibonachi(4) == 2
    assert fibonachi(5) == 3
    assert fibonachi(6) == 5

if __name__ == "__main__":
    pytest.main()