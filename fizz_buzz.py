import numpy
import math

def fizz_buzz(max_num, fizz_value, buzz_value):
    for num in range(1, max_num + 1):
        if num % fizz_value == 0 and num % buzz_value == 0:
            print('FizzBuzz')
        elif num % fizz_value == 0:
            print('Fizz')
        elif num % buzz_value == 0:
            print('Buzz')
        else:
            print(num)

fizz_buzz(100, 3, 5)