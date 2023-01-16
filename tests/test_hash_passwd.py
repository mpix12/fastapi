from passlib.context import CryptContext
import hash_passwd
import unittest


class testHash(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_passwd = 'passwd@1234'
        self.passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.passwd = self.passwd_context.hash(self.raw_passwd)

    def tearDown(self) -> None:
        print("tear down")

    def test_bcrypt_passwd(self):
        self.assertNotEqual(self.passwd, hash_passwd.bcrypt_passwd(self.raw_passwd))


if "__name__" == "__main__":
    unittest.run()


