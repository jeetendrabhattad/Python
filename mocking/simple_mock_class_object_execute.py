from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
# creating the mock object
fooObj = Foo()
#print fooObj
 
mockFoo = Mock(return_value = fooObj)
print mockFoo
 
# creating an "instance"
mockObj = mockFoo()
print mockObj
 
# working with the mocked instance
print mockObj._fooValue
mockObj.callFoo()
mockObj.doFoo("narf")
