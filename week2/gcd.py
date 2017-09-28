# Uses python3
'''
Created on Sep 26, 2017

@author: DeokJae - github.com/deokjj
'''
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euclidean(a,b):
    if a < b:
        return gcd_euclidean(b, a)
    if b == 0:
        return a 
    
    reminder = a % b
    return gcd_euclidean(b, reminder)

if __name__ == "__main__":
    input = sys.stdin.read()  # @ReservedAssignment
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))
