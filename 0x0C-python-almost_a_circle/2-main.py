#!/usr/bin/python3
""" 2-main.py """
from models.rectangle import Rectangle

if __name__ == '__main__':
    try:
        r = Rectangle(10, 2)
        r.width = '2'
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        Rectangle(10, 2)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        r = Rectangle(10, 2)
        r.x = "ok"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
