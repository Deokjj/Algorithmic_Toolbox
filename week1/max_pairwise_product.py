#python3
'''
Created on Sep 23, 2017

@author: DeokJae - github.com/deokjj
'''
from random import randint

# slower algorithm n^2 
def max_pairwise_product(a, n):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

# faster algorithm n
def max_pairwise_product_fast(a,n):
    maxIndex1 = int(-1)
    for i in range(0,n):
        if maxIndex1 == -1 or a[i] > a[maxIndex1]:
            maxIndex1 = i 
            
    maxIndex2 = int(-1)
    for i in range(0,n):
        if i != maxIndex1 and ( maxIndex2 == -1 or a[i] > a[maxIndex2] ):
            maxIndex2 = i 
    
#     print("from fast->")
#     print("maxIndex1: ",maxIndex1, ", maxIndex2: ",maxIndex2)
    return a[maxIndex1] * a[maxIndex2]

def submit():
    ''' Difference between sys.stdin.read() & input():
    sys.stdin.read(), you can add new lines, input() processes as input and enter key pressed'''
    n = int(input())
    a = [int(x) for x in input().split()]
       
    assert(len(a) == n) #assert(condition) triggers an error when condition is false.
    
    print(max_pairwise_product_fast(a,n));

def stress_test():
    from sys import maxsize # max avail integer number for int type
    
    while True:
        n = randint(0,maxsize) % 10 +2
        a = [randint(0,maxsize) % 100000 for i in range(0, n)]
        resultReg = max_pairwise_product(a,n)
        resultFast = max_pairwise_product_fast(a,n)
        if resultReg == resultFast:
            print('Okay')
        else:
            print('Wrong Answer')
            print("max_pairwise_product(a,n):", resultReg)
            print("max_pairwise_product_fast(a,n):", resultFast)
            print(a)
            return  
    
# stress_test()
submit()
