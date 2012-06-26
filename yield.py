from __future__ import generators

def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b

def main():
    fun = fib()
    for i in range(1,100):
        if i == 50:
            print fun.send(3)

        print fun.next()


if __name__ == "__main__":
    main()

