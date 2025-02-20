def reverse(a):
    for i in range(0, int(len(array)/2)):
        temp = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp
    

array = input("Enter a list of numbers separated by commas: ")
array = [int(x) for x in array.split(",")]

reverse(array)
print ("\nThe reversed list is: ", array)

# an algorithm to reverse an array