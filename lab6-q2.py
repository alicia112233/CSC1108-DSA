count = {}

# swap elements at index i and j or array a
def swap(a, i, j):
  global count
  a[i], a[j] = a[j], a[i]
  count[a[i]] = count[a[i]] + 1
  count[a[j]] = count[a[j]] + 1

# implement insertion sort that sorts an input array a using the swap
# function defined above to swap two elements of an array. 
# The swap function will automatically keep track of the number of 
# swap for each item.

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            swap(a, j, j - 1)
            j -= 1
        print(a)

# get user input
array = input("Enter a list of string to sort separated by commas:\n")
array = [str(x) for x in array.split(",")]

# set up the dictionary to track counts
for x in array:
  count[x] = 0
  
print(array)
insertionSort(array)
print("Number of swap for each item:", count)
total = 0
for i in count.keys():
  total = total + count[i]
print("Average number of swap for each item:", round((total*1.0)/len(count.keys()), 1))