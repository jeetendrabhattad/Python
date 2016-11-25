from mock import *

class SomeClass:
    attribute = 0

@patch.object(SomeClass, 'attribute', "hello")
def test():
    print SomeClass.attribute
    assert SomeClass.attribute != "hello"

test()
