#!/usr/bin/env
def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2) + 1):
            if (number % i) == 0:
                print("{} is not a prime number".format(number))
                break
        else:
            print("{} is a prime number".format(number))
    else:
        print("{} is a prime number".format(number))