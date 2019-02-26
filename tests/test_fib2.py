import pytest

from mypkg.fibonacci import fibonacci

def test_fib_10():
	assert(fibonacci(10) == 551)
print("This is just a test to see if it goes through multiple automatcially)
