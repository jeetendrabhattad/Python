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
 
mockFoo.doFoo("narf")
mockFoo.doFoo.assert_called_with("narf")
# assertion passes
 
mockFoo.doFoo("zort")
mockFoo.doFoo.assert_called_with("narf")
# AssertionError: Expected call: doFoo('narf')
# Actual call: doFoo('zort')
