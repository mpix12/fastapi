"""
Utility to decrypt and verify plain text password
"""

from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt_passwd(passwd):
    """
    Encrypt password
    :param passwd: plain text password
    :return: Hashed password
    """
    return passwd_context.hash(passwd)


def verify(hashed_passwd: str, plain_passwd: str):
    """
    Verify plain text and hashed password
    :param hashed_passwd: Hashed password
    :param plain_passwd: plain test password
    :return: Boolean values: True or False
    """
    return passwd_context.verify(plain_passwd, hashed_passwd)
