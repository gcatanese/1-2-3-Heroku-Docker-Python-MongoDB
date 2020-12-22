import unittest

from dao.db_client import *


class DbClientTest(unittest.TestCase):

    def test_get_user_by_name(self):
        ret = get_user_by_name('test')

        self.assertIsNotNone(ret)

    def test_add_user(self):
        ret = add_user('test')

        self.assertIsNotNone(ret)
