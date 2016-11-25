from mock import Mock, call
 
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
 
mockFoo.callFoo()
mockFoo.doFoo("narf")
mockFoo.doFoo("zort")
 
fooCalls = [call.callFoo(), call.doFoo("narf"), call.doFoo("zort")]
mockFoo.assert_has_calls(fooCalls)
# assert passes
 
#fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
#mockFoo.assert_has_calls(fooCalls)
# AssertionError: Calls not found.
# Expected: [call.callFoo(), call.doFoo('zort'), call.doFoo('narf')]
# Actual: [call.callFoo(), call.doFoo('narf'), call.doFoo('zort')]
 
fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
mockFoo.assert_has_calls(fooCalls, any_order = True)
# assert passes
