import unittest
import pytest

# Unit testing using unittest and pytest
def func(x):
    return x+1

# 3+1 == 5 = FAILED
# 4+1 == 5 = PASSED
def test_answer():
    assert func(3) == 5


if __name__ == "__main__":
    test_answer()