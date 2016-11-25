from mock import Mock
 
# The class interfaces
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue    
 
# create the mock object
mockFoo = Mock(spec = Foo)
 
# accessing the mocked attributes
print mockFoo
print mockFoo._fooValue
print mockFoo.callFoo()
 
mockFoo.callFoo()
# nothing happens, which is fine
