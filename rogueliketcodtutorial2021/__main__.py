import sys

from rogueliketcodtutorial2021.rogueliketcodtutorial2021 import fib, main

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
        print(fib(n))
    else:
        main()
