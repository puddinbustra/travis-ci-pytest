import pytest

from mypkg.fibonacci import fibonacci

print("Test_fib is running")

def test_fib_10():
	assert(fibonacci(10) == 550)

def test_fib_not_20():
	assert(fibonacci(20) != 20)	
