# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclidean(a,b):
    if a < b:
        return gcd_euclidean(b, a)
    if b == 0:
        return a 
    
    reminder = a % b
    return gcd_euclidean(b, reminder)

def lcm_fast(a, b):
    gcd = gcd_euclidean(a, b)
    return a*b//gcd

if __name__ == '__main__':
    input = sys.stdin.read()  # @ReservedAssignment
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

