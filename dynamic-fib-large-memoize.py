A=[0,1,1]
def fib(n):
    
    for i in range(3, n+1):
     
        if len(A) <= i:
            A.append(A[(i-1)] + A[(i-2)])




    return A[n]

print (fib(30))
print("______________")
print (fib(32))
print("++++++++++++++++++++++++++++++++++++++++++++++")
print (fib(40))
