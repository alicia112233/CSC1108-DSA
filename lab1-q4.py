def orderInsert(a, value):
    for i in range(0, len(a)-1):
        if a[i] > value:
            a.insert(i, value)
            return
    a.append(value)

array = input("Enter a list of numbers in increasing order separated by commas:\n")
array = [int(x) for x in array.split(",")]

value = int(input("Enter a number to insert into the array:\n"))

orderInsert(array, int(value))
print ("\nThe sorted list is: ", array)

# an algorithm to insert a number into a sorted array