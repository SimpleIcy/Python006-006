import re


# https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
phone_compiler = re.compile(r'^1(3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8[0-9]|9[0-9])\d{8}$')
email_compiler = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
email_compiler1 = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# password checker


def check_len(pwd):
    return len(pwd) >= 8


def check_contain_upper(pwd):
    pattern = re.compile('[A-Z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        return False


def check_contain_num(pwd):
    pattern = re.compile('[0-9]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        return False


def check_contain_lower(pwd):
    pattern = re.compile('[a-z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        return False


def check_symbol(pwd):
    pattern = re.compile('([^a-z0-9A-Z])+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        return False


def check_password(pwd):
    # 判断密码长度是否合法
    len_ok = check_len(pwd)
    # 判断是否包含大写字母
    upper_ok = check_contain_upper(pwd)
    # 判断是否包含小写字母
    lower_ok = check_contain_lower(pwd)
    # 判断是否包含数字
    num_ok = check_contain_num(pwd)
    # 判断是否包含符号
    symbol_ok = check_symbol(pwd)
    print(len_ok)
    print(upper_ok)
    print(lower_ok)
    print(num_ok)
    print(symbol_ok)
    return len_ok and upper_ok and lower_ok and num_ok and symbol_ok


def main():
    if check_password('Helloworld#123'):
        print('检测通过')
    else:
        print('检测未通过')
