import hashlib
import re
import time
from lxml import etree


def get_full_analysis(analysis):

    res_full = re.match(".*试题分析：(.*)考点：(.*)点评：(.*)", analysis)

    res_second = re.match(".*试题分析：(.*)考点：(.*)", analysis)

    res_first = re.match(".*试题分析：(.*)", analysis)

    if res_full:
        question_analysis = res_full.group(1)
        question_point = res_full.group(2)
        question_comment = res_full.group(3)
        return {
            "original": analysis,
            "question_analysis": question_analysis,
            "question_point": question_point,
            "question_comment": question_comment
        }
    elif res_second:
        question_analysis = res_second.group(1)
        question_point = res_second.group(2)
        question_comment = None
        return {
            "original": analysis,
            "question_analysis": question_analysis,
            "question_point": question_point,
            "question_comment": question_comment
        }
    elif res_first:
        question_analysis = res_first.group(1)
        question_point = None
        question_comment = None
        return {
            "original": analysis,
            "question_analysis": question_analysis,
            "question_point": question_point,
            "question_comment": question_comment
        }
    else:
        return {
            "original": analysis,
            "question_analysis": None,
            "question_point": None,
            "question_comment": None
        }
    pass


def deal_jam(choose_item):
    jam_list = ['this_jammer', 'hidejammersa', 'jammerd42', 'jammerd0o', 'labeljammerd0o']

    p = etree.HTML(choose_item)

    for jam in jam_list:
        l = p.xpath("//*[@class='%s']" % jam)
        for i in l:
            i.getparent().remove(i)

    res = etree.tostring(p, encoding="utf-8").decode('utf-8').replace('<html><body>', '').replace('</body></html>', '')
    return res


def replace_i(s):
    res = re.match("^<i>(.*)</i>$", s)

    if res:
        return "<p>" + res.group(1) + "</p>"
    else:
        return s
    pass


def from_content_get_real_content(dt):
    dt = dt.replace('\n', '')

    res = re.match("^<dt>(.*)</dt>$", dt)

    if res:
        return res.group(1)
    else:
        return dt
    pass


def from_choose_item_get_content(td):
    res = re.match("^<td.*?>(.*)</td>$", td)

    if res:
        return res.group(1)
    else:
        return td
    pass


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
