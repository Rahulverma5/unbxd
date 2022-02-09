# def fact(n):  
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n * fact(n - 1) 

def TrailingZeros(n):
    z=0
    while True:
        if n%10 == 0:
            z+=1
        else:
            break
    return z
# n=fact(10)
print(TrailingZeros(100)) 