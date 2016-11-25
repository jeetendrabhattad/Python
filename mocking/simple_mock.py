from mock import MagicMock
 
# prepare the spec list
fooSpec = ["_fooValue", "callFoo", "doFoo"]
 
# create the mock object
mockFoo = MagicMock(spec = fooSpec)
# accessing the mocked attributes
print mockFoo
print mockFoo._fooValue
print mockFoo.callFoo()
 
# nothing happens, which is fine
mockFoo.callFoo()

