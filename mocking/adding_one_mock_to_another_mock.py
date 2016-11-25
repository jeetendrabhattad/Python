from mock import Mock
 
# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
class Bar(object):
    # instance properties
    _barValue = 456
     
    def callBar(self):
        pass
     
    def doBar(self, argValue):
        pass
 
# create the first mock object
mockFoo = Mock(spec = Foo)
print mockFoo
 
# create the second mock object
mockBar = Mock(spec = Bar)
print mockBar
 
# attach the second mock to the first
mockFoo.attach_mock(mockBar, 'fooBar')
 
# access the first mock's attributes
print mockFoo
print mockFoo._fooValue
print mockFoo.callFoo()
 
# access the second mock and its attributes
print mockFoo.fooBar
print mockFoo.fooBar._barValue
print mockFoo.fooBar.callBar()
print mockFoo.fooBar.doBar("narf")
