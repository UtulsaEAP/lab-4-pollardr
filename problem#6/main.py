# Riley Pollard
# Thursday lab 2pm, Wednesday class

def fibonacci(n):
    #write your code here
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    i = 0
    j = 1
    count = 2
    
    fib = 0
    while count <= n:
        
        fib = i + j
        
        i = j
        j = fib
        count +=1
    return fib
if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')