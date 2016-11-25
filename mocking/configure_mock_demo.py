from mock import Mock
'''
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
mockFoo = Mock(spec = Foo, return_value = 555)
print mockFoo()
# returns: 555
 
mockFoo.configure_mock(return_value = 999)
print mockFoo()
# returns: 999
'''
class Database(object):
    def insert(self):
        pass
mockFoo = Mock(spec = Database)
fooSpec = {'insert.return_value':"true"}
mockFoo.configure_mock(**fooSpec)
print mockFoo.insert()
fooSpec = {'insert.side_effect':StandardError}
try:
    mockFoo.configure_mock(**fooSpec)
    print mockFoo.insert()
except StandardError as e:
    print("Test Passed")
#fooSpec = {'callFoo.return_value':"narf", 'doFoo.return_value':"zort", 'doFoo.side_effect':StandardError}
#mockFoo = Mock(spec = fooSpec, return_value = 555)
 
# returns: narf
#print mockFoo.doFoo("narf")
# raises: StandardError
 
#fooSpec = {'doFoo.side_effect':None}
#mockFoo.configure_mock(**fooSpec)
#print mockFoo.doFoo("narf")
# returns: zort
