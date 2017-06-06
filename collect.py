# -*- coding: UTF-8 -*-
from information_collect import information_main
from shortname import short

def banner():
    print(colour.yellow)
    print("=======================================================")
    print("             coding by bfpiaoran@qq.com")
    print("-------------------------------------------------------")
    print("            a simple gadget for security")
    print("=======================================================")
    print("")

class colour:
    pink = "\033[95m"
    blue = "\033[94m"
    yellow = "\033[93m"
    green = "\033[92m"
    red = "\033[91m"
    white = "\033[97m"


def choice():
    way = input(colour.white+" 1 information collect \n 2 Short domain name \n 3 Network request\n")
    print(colour.green)
    try:
        way = int(way)
    except Exception as e:
        print('please enter a number')
        print(e)
    if way == 1:
        information_main.main()
    if way == 2:
        short.main()


def main():
    banner()
    stop = 'a'
    while stop != 'q':
        choice()
        stop = input('Enter q to exit \n')
    print(' good bye ')
if __name__ == '__main__':
    main()