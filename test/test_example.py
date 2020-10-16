import unittest
from unittest.mock import patch
from test.test_class import Foo

class TestStringMethods(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    @patch('test.test_class.Foo.say')
    def test_patch(self, mock_say):
        foo = Foo()
        word = foo.say()
        print(word) # <MagicMock name='say()' id='140279777029456'>

    @patch('test.test_class.Foo.say', return_value = 'beer')
    def test_patch_return_value(self, mock_say):
        foo = Foo()
        word = foo.say()
        self.assertEqual(word, 'beer')

    @patch('test.test_class.Foo.say')
    def test_patch_non_existant_method(self, mock_foo):
        foo = Foo()
        print(foo)
        with self.assertRaises(TypeError):
            word = foo.sayo()

if __name__ == '__main__':
    unittest.main()