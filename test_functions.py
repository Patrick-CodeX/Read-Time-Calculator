# test_functions_pytest.py
import pytest
import os
from main import *

# Test for factorial function
def test_factorial():
    assert factorial(5) == 120  # 5! = 120
    assert factorial(0) == 1    # 0! = 1
    assert factorial(1) == 1    # 1! = 1
    assert factorial(3) == 6    # 3! = 6

    # Test for exception on negative input
    with pytest.raises(ValueError):
        factorial(-5)

# Test for maxOfThree function
def test_maxOfThree():
    assert maxOfThree(1, 2, 3) == 3
    assert maxOfThree(-1, -2, -3) == -1
    assert maxOfThree(5, 10, 7) == 10
    assert maxOfThree(3, 3, 3) == 3

def test_readingCalc():
    # Call the function
    result = readingCalculator('file.txt')

    # Expected output: (700, 'words', '2', 'minute read')
    expected = (f"{result[0]} {result[1]}, a {result[2]} {result[3]}.")
    assert result == expected  # Assert that the result matches expected

    # Clean up the test file
    os.remove('file.txt')