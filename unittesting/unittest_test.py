import unittest

class StringMethods(unittest.TestCase):

    def test_upper(self):
        #obj = Person()
        #self.assertTrue(obj.IsEmployeed())
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("Verifying for isupper")
        self.assertTrue('FOO'.islower())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        #with self.assertRaises(TypeError):
        #    s.split(2)
    def test(self):
        print "Hello"

    def runTest(self):
        print("inside run")
        self.test_split()
        self.test()
        self.test_isupper()
        #print args, kwargs
        #StringMethods.test_split(args[0])

if __name__ == '__main__':
    unittest.main() # run
    #obj = StringMethods()
    #obj.run()
    
