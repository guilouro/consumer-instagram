# coding: utf-8

from app import app
import unittest


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_index(self):
        self.index = self.client.get('/')
        self.assertEqual(self.index.status_code, 200)


if __name__ == '__main__':
    unittest.main()
