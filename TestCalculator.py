import pytest
from Task4 import calculator

def testCalculator():
    result1 = calculator(1, 2, "+")
    assert result1 == 3
    result2 = calculator(10, 2, "-")
    assert result2 == 8
    result3 = calculator(5, 2, "*")
    assert result3 == 10
    result4 = calculator(2, 2, "/")
    assert result4 == 1


if __name__ == "__main__":
    pytest.main()