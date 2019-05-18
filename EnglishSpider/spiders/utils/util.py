import hashlib
import time


def md5(s):
    m2 = hashlib.md5()
    m2.update(s.encode('utf-8'))
    return str(m2.hexdigest())


def datetime_format_str():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
