def find2Smallest(a):
    if a[0] < a[1]:
        smallest = a[0]
        secondSmallest = a[1]

    else:
        smallest = a[1]
        secondSmallest = a[0]

    for i in range(2, len(a)):
        if a[i] < smallest:
            secondSmallest = smallest
            smallest = a[i]
        elif a[i] < secondSmallest:
            secondSmallest = a[i]

    return smallest, secondSmallest

array = input("Enter a list of numbers separated by commas:\n")
array = [int(x) for x in array.split(",")]

print("The 2 smallest values are: ", find2Smallest(array))

# an algorithm to find the 2 smallest values in an array