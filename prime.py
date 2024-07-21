import math
import sys


b = 0
a = 3 + 2 * b
# argument value - argv

def prime(number):
    if number <= 1:
        return False
        print('这个数不是素数')
    elif number == 2:
        return True
        print('这个数是素数')
    elif number % 2 == 0:
        return False
        print('这个数不是素数')
    while number % a != 0:
        b + 1
    if number % a == 0:
        return False
        print('这个数不是素数')

if __name__ == "__main__":
    print("请输入一个数字：")
    first_param = sys.argv[1]
    prime(first_param)