import hashlib
import re
import time


def md5(s):
    m2 = hashlib.md5()
    m2.update(s.encode('utf-8'))
    return str(m2.hexdigest())


def datetime_format_str():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def deal_erji_raw_str(raw_str):
    """
    处理二级标题
    :param raw_str:
    :return:
    """
    resu = re.match("考点：(.*)", raw_str)

    if resu:
        return str(resu.group(1))
    else:
        return "N/A"
    pass


def get_last_number(n):
    resp = re.match(".*?(\d+)", n)
    if resp:
        return resp.group(1)
    else:
        return -1
    pass