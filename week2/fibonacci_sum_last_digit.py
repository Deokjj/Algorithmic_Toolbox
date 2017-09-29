# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n + 1): 
        previous, current = current, (previous + current) % 10
    # end of the loop, current is fib_lastdigit[n+2]
    
    return current -1

if __name__ == '__main__':
    input = sys.stdin.read()  # @ReservedAssignment
    n = int(input)
    print(fibonacci_sum_fast(n))
