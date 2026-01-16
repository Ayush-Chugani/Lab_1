# app.py
import sys

def square(num):
    return num * num

if __name__ == "__main__":
    num = int(sys.argv[1])
    print("Square of the number is", square(num))