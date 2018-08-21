#!/usr/bin/python

import random


class Number():

    def __init__(self):
        self.num = random.randint(1,100)


    def recurs(self,guess):
        count = 0
        while True:
            if self.num > guess:
                print "higher"
                guess = input()
                count += 1
                continue
            elif self.num < guess:
                print "lower"
                guess = input()
                count += 1
                continue
            elif self.num == guess:
                print "correct, you used ",count,"tries"
                return True

if __name__ == "__main__":
    n = Number()
    print "Guess a number 1-100:"
    guess = input()
    while guess>100 or guess<0:
        print "retry"
        guess = int(raw_input())


    bool = n.recurs(guess)
    if bool == True:
        exit()
