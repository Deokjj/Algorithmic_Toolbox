# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum_pisano(from_, to):
    previous = 0
    current  = 1
    
    pisanoSq = [0,1]

    for _ in range(2,to + 3):
        previous, current = current, previous + current # after this line, previous is i+1th fib and current is i+2th fib
        newPisano = current % 10
        
        if newPisano == 1 and pisanoSq[-1] == 0: # '01' found
            del pisanoSq[-1] # deletes last element which is the start of the sequence
            nOfSq = len(pisanoSq)
            return (pisanoSq[(to+2) % nOfSq] - pisanoSq[(from_ +1) % nOfSq]) % 10
        else:
            pisanoSq.append(newPisano) # add to the sequence
            
    return (pisanoSq[-1] -pisanoSq[from_+1]) % 10 #returns the last element when the sequence has not been completed after nth iteration.


if __name__ == '__main__':
    input = sys.stdin.read();  # @ReservedAssignment
    from_, to = map(int, input.split())
#     print("fibonacci_partial_sum_naive(from_, to): ",fibonacci_partial_sum_naive(from_, to))
#     print("fibonacci_partial_sum_pisano(from_, to): ", fibonacci_partial_sum_pisano(from_, to))
    print(fibonacci_partial_sum_pisano(from_, to))