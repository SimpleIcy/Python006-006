import datetime
from time import sleep
import logging
from random import randint


file_date_fix = datetime.datetime.now().strftime('%Y-%m-%d')
log_file_name = 'python-%s.log' % file_date_fix
logging.basicConfig(filename=log_file_name, format='%(asctime)s %(message)s', level=logging.DEBUG)


def special_function(times=10):
    """ 此函数在调用时，会将进入函数的时间和出去函数的时间记录到日志，日志路径
    为程序运行目录，日志名为python-xxxx-xx-xx-xxxxxx.log"""
    enter_msg = '你调用了函数%s。' % special_function.__name__
    logging.debug(msg=enter_msg)
    for i in range(times):
        sleep_time = randint(1, 3)
        print('先睡上%s秒！' % sleep_time)
        sleep(sleep_time)
    exit_msg = '函数调用完成，离开函数。'
    logging.debug(msg=exit_msg)


if __name__ == '__main__':
    call_times = int(input('调用函数次数：'))
    for i in range(call_times):
        special_function(4)
