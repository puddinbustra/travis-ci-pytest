import pytest
from src.fibonacci import fibonacci
#from mypkg.fibonacci import fibonacci



def test_fib_10():
	assert(fibonacci(10) == 10)

def test_fib_not_20():
	assert(fibonacci(20) != 20)	
