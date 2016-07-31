from interpreter import run, parse
import unittest

class TestInterpreter(unittest.TestCase):
    def test_should_be_hello_world(self):
        code = '+++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.------------.<++++++++.--------.+++.------.--------.>+.'
        self.assertEqual(run(parse(code)),
                         'Hello, world!')

    def test_ignore_space(self):
        code = '  +++  \n--- '
        self.assertEqual(parse(code), ['+', '+', '+', '-', '-', '-'])


if __name__ == '__main__':
    unittest.main()
