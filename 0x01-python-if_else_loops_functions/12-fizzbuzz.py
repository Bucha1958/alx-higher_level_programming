#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        if i == 0:
            continue
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        if i % 3 == 0:
                print("Fizz", end=" ")
        if i % 5 == 0:
                print("Buzz", end=" ")
        else:
            print("{} ".format(i), end=" ")
