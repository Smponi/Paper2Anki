import unittest

from starlette.testclient import TestClient

import Paper2Anki.main

"""
Module to test the implemented fastapi
"""


class MyTestCase(unittest.TestCase):
    test_app = TestClient(Paper2Anki.main.app)

    def test_get_response(self):
        response = self.test_app.get("/")
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()
