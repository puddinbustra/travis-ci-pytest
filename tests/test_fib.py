import pytest
#from mypkg.fibonacci import fibonacci
from mypkg.happy import happy


def test_fib_10():
	assert(happy(10) == 55)

