# Uses python3
'''
Created on Sep 26, 2017

@author: DeokJae - github.com/deokjj
'''
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    if(n<=1):
        return n
    
    fibArray = [0,1]
    for i in range(2,n+1):
        fibArray.append( fibArray[i-2] + fibArray[i-1] ) 
    return fibArray[n]

n = int(input())
# print(calc_fib(n))
print(calc_fib_fast(n))