from mock import Mock
 
# The mock specification
class Foo(object):
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
mockFoo.doFoo("narf")
mockFoo.doFoo("zort")
 
mockFoo.callFoo.assert_any_call()
# assert passes
mockFoo.doFoo("troz")
 
mockFoo.doFoo.assert_any_call("zort")
# assert passes
 
mockFoo.doFoo.assert_any_call("egad")
# raises: AssertionError: doFoo('egad') call not found
