# coding: utf-8

from app import app
import unittest


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_index(self):
        self.index = self.client.get('/')
        self.assertEqual(self.index.status_code, 200)

    def test_get_callback(self):
        self.callback = self.client.get(
            '/auth_callback',
            data=dict(code='5bcee29da146435882b9d4fbb988bd98')
        )
        self.assertEqual(self.callback.status_code, 302)

    def test_get_callback_bad_request(self):
        self.callback = self.client.get('/auth_callback')
        self.assertEqual(self.callback.status_code, 400)

    def test_get_callback_missing(self):
        self.callback = self.client.get(
            '/auth_callback',
            data=dict(code='')
        )
        self.assertEqual(self.callback.status_code, 200)


if __name__ == '__main__':
    unittest.main()
