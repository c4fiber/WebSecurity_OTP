import time
import hashlib
import random
import requests
from datetime import datetime

def getUnixTimeNow():
    tm = int(time.time())
    return str(tm)

def setSerial(text):
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


def getOTP(serial, name, sendIt, tm):
    if tm is int:
        tm = str(tm)

    if int(tm) < 0:
        tm = getUnixTimeNow()

    # SERVER쪽 DB는 이미 md5 해쉬화 한 값을 사용하므로, 클라이언트쪽 요청일 경우 미리 한번 해시화
    if (len(serial) != 32):
        serial = md5Hashing(serial)
    
    if sendIt:
        r = requests.get("http://127.0.0.1/gnuboard4/otp.php?serial="+serial+"&id="+name+"&time="+tm)

    key1 = md5Hashing(tm)
    key2 = serial

    random.seed(getSeed(key1, key2))
    otp = random.randrange(123456,987654)
    
    print(otp) # php print 결과 획득용

    return otp

if __name__ == '__main__':
    name = "victim"
    serial = "absde2kj32d1"

    getOTP(serial, name, False, -1)