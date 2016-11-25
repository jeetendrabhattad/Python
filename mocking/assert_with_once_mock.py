from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        pass
     
    def doFoo(self, argValue):
        pass
 
# create the mock object
mockFoo = Mock(spec = Foo)
print mockFoo
# returns <Mock spec='Foo' id='507120'>
 
mockFoo.callFoo()
mockFoo.callFoo.assert_called_once_with()
# assertion passes
 
mockFoo.callFoo()
mockFoo.callFoo.assert_called_once_with()
# AssertionError: Expected to be called once. Called 2 times.
