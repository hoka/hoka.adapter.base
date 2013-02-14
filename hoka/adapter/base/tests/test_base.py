import unittest
from hoka.adapter.base import BaseAdapter

class TestBase(unittest.TestCase):

    def test_sample(self):
        BaseAdapter(object())

if __name__ == '__main__':
    unittest.main()
