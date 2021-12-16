def digits_sum(n):
    s = 0
    while n > 9:
        s += n % 10
        n //= 10
    s += n
    return s


def super_digit(n):
    p = digits_sum(n)
    if p < 10:
        return p
    return super_digit(p)


def super_digit_iter(n):
    p = digits_sum(n)
    while p > 9:
        p = digits_sum(p)
    return p


def main():
    n, k = map(int, input("Enter the numbers: ").strip().split(' '))
    print("The Super Digit : ", super_digit_iter(digits_sum(n) * k))


if __name__ == "__main__":
    main()
    
    
    
    
    """
    [summary]
    Test Case : -> Expected Answer
    1. 975 4 -> 3
    2. 123 3 -> 9
    3. 567 8 -> 9
    """
    
    