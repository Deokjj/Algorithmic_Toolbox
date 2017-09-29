# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_pisano(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    pisanoSq = [0,1]

    for i in range(2,n + 1):
        previous, current = current, previous + current # after this line, previous is i-1th fib and current is ith fib
        newPisano = current % m
        
        if newPisano == 1 and pisanoSq[-1] == 0: # '01' found
            del pisanoSq[-1] # deletes last element which is the start of the sequence
            nOfSq = len(pisanoSq)
            return pisanoSq[n % nOfSq]
        else:
            pisanoSq.append(newPisano) # add to the sequence
            
    return pisanoSq[-1] #returns the last element when the sequence has not been completed after nth iteration.

if __name__ == '__main__':
    input = sys.stdin.read();  # @ReservedAssignment
    n, m = map(int, input.split())
    print(get_fibonacci_huge_pisano(n, m))
