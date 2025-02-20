def GCD(n, m):
    if m<n and n%m == 0:
        return m
    elif n<m:
        return GCD(m, n)
    else:
        return GCD(m, n%m)

print(GCD(54, 24))

# recursive function for GCD