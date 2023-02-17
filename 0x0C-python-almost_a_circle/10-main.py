#!/usr/bin/python3

from models.square import Square

""" 12-main.py """

if __name__ == "__main__":

    r1 = Square(5)
    print(r1)
    print(r1.size)
    r1.size = 10
    print(r1)

    try:
        r1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
