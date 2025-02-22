count = {}

# swap elements at index i and j or array a
def swap(a, i, j):
  global count
  a[i], a[j] = a[j], a[i]

  count[a[i]] = count[a[i]] + 1
  count[a[j]] = count[a[j]] + 1

# implement selection sort
# use the swap function defined above to swap two elements of an array. 
# The swap function will automatically keep track of
# the number of swap for each item

def selectionSort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        
        # Swap if a smaller element is found
        if min_index != i:
            swap(a, i, min_index)
  
# get user input
array = input("Enter a list of string to sort separated by commas:\n")
array = [str(x) for x in array.split(",")]

# set up the dictionary to track counts
for x in array:
  count[x] = 0

selectionSort(array)
print("Number of swap for each item:", count)
total = 0
for i in count.keys():
  total = total + count[i]
print("Average number of swap for each item:", (total*1.0)/len(count.keys()))