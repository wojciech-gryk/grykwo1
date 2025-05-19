def hello():
    print("hello world")

def hello2():
    print("hi, my name is.....")

def caller(f):
    return f

if __name__ == '__main__':
    hello()
    hello2()
    caller(1)