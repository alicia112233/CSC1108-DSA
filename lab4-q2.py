def sumNTerm(n):
    if n == 1:
        return 1.0
    elif n%2 == 0:
        return (1.0/n) + sumNTerm(n-1)
    else:
        return sumNTerm(n-1) - (1.0/n)
    
print(sumNTerm(5))

# to find n terms of the series