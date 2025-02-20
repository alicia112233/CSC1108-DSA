def findLargestIndex(a):
    largest = a[0]
    largestIndex = 0
    for i in range(1, len(a)):
        if a[i] > largest:
            largest = a[i]
            largestIndex = i
    return largestIndex

array = input("Enter a list of numbers separated by commas: ")
array = [int(x) for x in array.split(",")]

largestIndex = findLargestIndex(array)

print ("\nThe largest number is %d at index %d" %(array[largestIndex], largestIndex))

# an algorithm to find the index of the first largest number in an array