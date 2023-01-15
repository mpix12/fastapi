from passlib.context import CryptContext


passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt_passwd(passwd):
    return passwd_context.hash(passwd)


def verify(hashed_passwd: str, plain_passwd: str):
    return passwd_context.verify(plain_passwd, hashed_passwd)
