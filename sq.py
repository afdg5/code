#! /usr/bin/python


def fibo(num):
    if num<0:
        print "incorrect input"
    elif num==1 or num==0:
        return num
    elif num>1:
        return fibo(num-1) + fibo(num-2)

if __name__ == "__main__":
    print("enter number")
    value = fibo(input())
    print value
