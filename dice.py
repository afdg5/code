#! /usr/bin/python

import random

class DIE():

    def __init__(self):
        self.num = random.randint(1,6)




if __name__ == "__main__":
    while True:
        print "Would you like to roll the dice?? Y OR N"
        input = raw_input()

        if input == "N" or input == "n":
            break

        if input == "Y" or input == "y":
            d = DIE()
            print d.num
            continue
        else:
            print "sorry"
            continue
