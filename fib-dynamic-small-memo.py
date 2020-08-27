
def fib(n):
    A=[0,1]    
    for i in range(2, n+1):
        temp = A[0] + A[1]
        A[0] = A[1]
        A[1] = temp 
   
        
    return A[1]

print (fib(30))
print("______________")
print (fib(32))
print("++++++++++++++++++++++++++++++++++++++++++++++")
print (fib(40))
