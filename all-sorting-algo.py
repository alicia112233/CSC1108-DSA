# BUBBLE SORT
# Worst case --> O(n^2)
# Average case --> O(n^2)
# Best case --> O(n)
# same no. of comparisons with selection sort with lesser no. of swaps
# regardless of items arrangement, bubble sort always makes n-1 passes to sort n elements
# Space complexity: O(1)
def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubbleSort(aList))

# SELECTION SORT
# Worst case --> O(n^2)
# Average case --> O(n^2)
# Best case --> O(n^2)
# uses n-1 passes to sort n elements
# same no. of comparisons with bubble sort with lesser no. of swaps
# Space complexity: O(1)
def selectionSort(aList):
    for fillslot in range(len(aList)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location
        temp = aList[fillslot]
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp

aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(selectionSort(aList))

# INSERTION SORT
# Worst case --> O(n^2)
# Average case --> O(n^2)
# Best case --> O(n) when the list is already sorted
# uses n-1 passes to sort n elements
# Space complexity: O(1)
def insertionSort(aList):
    for index in range(1, len(aList)):
        currentvalue = aList[index]
        position = index
        while position > 0 and aList[position-1] > currentvalue:
            aList[position] = aList[position-1]
            position = position - 1
        aList[position] = currentvalue

aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertionSort(aList))

# MERGE SORT
# Divide and conquer algorithm
# Worst case --> O(nlogn)
# Average case --> O(nlogn)
# preferred for Linked List / larger array size
# uses log2(n) passes **round UP
# Space Complexity: O(n)
def merge(arrayA, arrayB):
    arrayC = []
    sizeA = len(arrayA)
    sizeB = len(arrayB)

    indexA = indexB = 0
    while indexA < sizeA and indexB < sizeB:
        if arrayA[indexA] < arrayB[indexB]:
            arrayC.append(arrayA[indexA])
            indexA += 1
        else:
            arrayC.append(arrayB[indexB])
            indexB += 1

    # Add remaining elements
    arrayC.extend(arrayA[indexA:])
    arrayC.extend(arrayB[indexB:])
    
    return arrayC

def mergeSort(array):
    size = len(array)

    if size == 1:
        return array
    
    midIndex = size // 2
    firstHalf = array[:midIndex]
    secondHalf = array[midIndex:]

    # Recursively sort and merge
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    return merge(firstHalf, secondHalf)

print(mergeSort([42, 24, 36, 36, 38, 44, 7, 10, 21, 17]))

# QUICK SORT:
# Divide and conquer algorithm
# Worst case --> O(n^2)
# Average case --> O(nlogn)
# same for number of passes^
# preferred for Arrays
# Space Complexity: O(logN)
def quickSort(array):
    size = len(array)
    if size > 1:
        pivotIndex = partition(array)
        array[0:pivotIndex] = quickSort(array[0:pivotIndex])
        array[pivotIndex+1:size] = quickSort(array[pivotIndex+1:size])
    return array

def partition(array):
    pivot = array[0]
    size = len(array)
    pivotIndex = 0
    for index in range(1, size):
        if array[index] < pivot:
            pivotIndex += 1
            array[index], array[pivotIndex] = array[pivotIndex], array[index]
    array[0], array[pivotIndex] = array[pivotIndex], array[0]
    return pivotIndex

print(quickSort([42, 24, 36, 36, 38, 44, 7, 10, 21, 17]))
