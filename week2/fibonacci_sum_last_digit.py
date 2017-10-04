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

def fibonacci_sum_pisano(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    pisanoSq = [0,1]

    for _ in range(n + 1):
        previous, current = current, previous + current # after this line, previous is i+1th fib and current is i+2th fib
        newPisano = current % 10
        
        if newPisano == 1 and pisanoSq[-1] == 0: # '01' found
            del pisanoSq[-1] # deletes last element which is the start of the sequence
            nOfSq = len(pisanoSq)
            return (pisanoSq[(n+2) % nOfSq] - 1) % 10
        else:
            pisanoSq.append(newPisano) # add to the sequence
            
    return (pisanoSq[-1] -1) % 10 #returns the last element when the sequence has not been completed after nth iteration.

if __name__ == '__main__':
    input = sys.stdin.read()  # @ReservedAssignment
    n = int(input)
    
    print(fibonacci_sum_pisano(n))
