def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    return next(i for i in range(n+1, 2*n) if is_prime(i))

def main():
    print(first_prime_over(1000000))

if __name__ == '__main__':
    main()