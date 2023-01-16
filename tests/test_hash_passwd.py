from passlib.context import CryptContext
import unittest
import sys

# from utilities import hash_passwd

sys.path.insert(0, '/var/jenkins_home/workspace/python\ build\ and\ test\ demo/utilities/hash_passwd')
# from utilities.hash_passwd import bcrypt_passwd


class testHash(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_passwd = 'passwd@1234'
        self.passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.passwd = self.passwd_context.hash(self.raw_passwd)

    def tearDown(self) -> None:
        print("tear down")

    def test_bcrypt_passwd(self):
        self.assertNotEqual(self.passwd, hash_passwd.bcrypt_passwd(self.raw_passwd))
