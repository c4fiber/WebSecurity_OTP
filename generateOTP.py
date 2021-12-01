import time
import hashlib
import random

serial = "ABCD1234EFGH"

def editSerial(text):
    try:
        if len(text) != 12:
            raise ValueError("length must be 12")
        serial = text
    except TypeError as e:
        print(e)


def md5Hashing(text):
    hash  = hashlib.md5()
    hash.update(text.encode('utf-8'))

    return hash.hexdigest()


def getSeed(key1, key2):
    seed = ''.join(filter(str.isdigit, key1+key2))
    if seed == '':
        seed = 0
    return seed


def getOTP():
    key1 = md5Hashing(str(time.time()))
    key2 = md5Hashing(serial)

    seed = getSeed(key1, key2)
    random.seed(seed)

    return random.randrange(123456,987654)
