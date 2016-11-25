from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
# creating the mock object (without a side effect)
fooObj = Foo()
 
mockFoo = Mock(return_value = fooObj)
print mockFoo
 
mockObj = mockFoo()
print mockObj
 
mockFoo = Mock(return_value = fooObj, side_effect = NameError)
obj = mockFoo()
# raises: NameError
