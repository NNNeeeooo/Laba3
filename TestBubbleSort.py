import pytest
from Task4 import bubbleSort

def testBubbleSort():
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    bubbleSort(arr1)
    assert arr1 == [1, 2, 3, 4, 5, 6, 7]

    arr2 = [7, 6, 5, 4, 3, 2, 1]
    bubbleSort(arr2)
    assert arr2 == [1, 2, 3, 4, 5, 6, 7]

if __name__ == "__main__":
    pytest.main()