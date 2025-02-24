Best case and Worst case complexity of carrying out linear search and binary search for the following input data:
<br>a. Unsorted array of N elements
<br>**Linear Search**
- Best Case: O(1) - if element is found at the 1st index!
- Worst Case: O(N) - if element is at the last index / not found :(

**Binary Search**
- Best & Worst Case: O(NlogN) - Not applicable unless sorted first!!

b. Sorted array of N elements
<br>**Linear Search**
- Best Case: O(1) - if element is found at the 1st index!
- Worst Case: O(N) - if element is at the last index / not found :(
  <br>--> same as unsorted array since linear search _doesn’t use **sorting**_

**Binary Search**
- Best Case: O(1) - if the element is found at the middle index in the first step.
- Worst Case: O(logN) - when the element is found **after** the **maximum** number of divisions or not found at all.
