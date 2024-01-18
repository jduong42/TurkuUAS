def factorials(n: int) -> dict:
    factorial_dict = {}
    factorial = 1

    for i in range(1, n+1):
        factorial = factorial * i
        factorial_dict[i] = factorial
    
    return factorial_dict

def main():
    pass
    print(factorials(5))

__init__ = main()