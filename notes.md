# SEARCHING ALGORITHMS
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

Given a hash table of **size 13**, show the contents of your hash table after inserting the values {8, 2, 7, 20, 33, 15, 19, 34, 12, 21} using the following:
<br>a. **Separate Chaining** with hash function h(x) = x mod 13.
<br>b. **Open Addressing** with linear probing with hash function h(x) = x mod 13

a) Separate Chaining
<br>Hash Values:
- h(8) = 8 % 13 = 8
- h(2) = 2 % 13 = 2
- h(7) = 7 % 13 = 7
- h(20) = 20 % 13 = 7
- h(33) = 33 % 13 = 7
- h(15) = 15 % 13 = 2
- h(19) = 19 % 13 = 6
- h(34) = 34 % 13 = 8
- h(12) = 12 % 13 = 12
- h(21) = 21 % 13 = 8

Table after insertion:
- Index 0: []
- Index 1: []
- Index 2: [2, 15]
- Index 3: []
- Index 4: []
- Index 5: []
- Index 6: [19]
- Index 7: [7, 20, 33]
- Index 8: [8, 34, 21]
- Index 9: []
- Index 10: []
- Index 11: []
- Index 12: [12]

<br>b) Open Addressing (Linear Probing)
<br>Hash Values:
- h(8) = 8 % 13 = 8 → Insert at index 8
- h(2) = 2 % 13 = 2 → Insert at index 2
- h(7) = 7 % 13 = 7 → Insert at index 7
- h(20) = 20 % 13 = 7 → Collision at index 7, insert at index 8 (next available spot)
- h(33) = 33 % 13 = 7 → Collision at index 7, check 8 → Collision, insert at index 9
- h(15) = 15 % 13 = 2 → Collision at index 2, check 3 → Insert at index 3
- h(19) = 19 % 13 = 6 → Insert at index 6
- h(34) = 34 % 13 = 8 → Collision at index 8, check 9 → Collision, check 10 → Insert at index 10
- h(12) = 12 % 13 = 12 → Insert at index 12
- h(21) = 21 % 13 = 8 → Collision at index 8, check 9 → Collision, check 10 → Collision, check 11 → Insert at index 11

Table after insertion:
- Index 0: []
- Index 1: []
- Index 2: [2]
- Index 3: [15]
- Index 4: []
- Index 5: []
- Index 6: [19]
- Index 7: [7]
- Index 8: [8]
- Index 9: [33]
- Index 10: [34]
- Index 11: [21]
- Index 12: [12]

<br>In closed hashing, Linear Probing tends to results in clustering of keys in certain region of the hash table. Other types of probe sequences such as Quadratic probing and Double Hashing can be used to reduce or eliminate the clustering effect.
<br>a. Using **Quadratic Probing**, with a hash table of **size 13** and a hash function **h(x)=x mod 13**
<br>i. Show the contents of the hash table after inserting the following sequence of values: 77, 94, 73, 90, 55, 51, 54, 76, 103
<br>Hash Values:
- h(77) = 77 % 13 = 12 → Insert at index 12
- h(94) = 94 % 13 = 3 → Insert at index 3
- h(73) = 73 % 13 = 8 → Insert at index 8
- h(90) = 90 % 13 = 12 → Collision at index 12
  - Probe 1: h(90, 1) = (12 + 1^2) % 13 = 13 % 13 = 0 → Insert at index 0
- h(55) = 55 % 13 = 3 → Collision at index 3
  - Probe 1: h(55, 1) = (3 + 1^2) % 13 = 4 → Insert at index 4
- h(51) = 51 % 13 = 12 → Collision at index 12
  - Probe 1: h(51, 1) = (12 + 1^2) % 13 = 0 → Collision at index 0
  - Probe 2: h(51, 2) = (12 + 2^2) % 13 = 8 → Collision at index 8
  - Probe 3: h(51, 3) = (12 + 3^2) % 13 = 5 → Insert at index 5
- h(54) = 54 % 13 = 2 → Insert at index 2
- h(76) = 76 % 13 = 11 → Insert at index 11
- h(103) = 103 % 13 = 12 → Collision at index 12
  - Probe 1: h(103, 1) = (12 + 1^2) % 13 = 0 → Collision at index 0
  - Probe 2: h(103, 2) = (12 + 2^2) % 13 = 8 → Collision at index 8
  - Probe 3: h(103, 3) = (12 + 3^2) % 13 = 5 → Collision at index 5
  - Probe 4: h(103, 4) = (12 + 4^2) % 13 = 12 → Collision at index 12
  - Probe 5: h(103, 5) = (12 + 5^2) % 13 = 2 → Collision at index 2
  - Probe 6: h(103, 6) = (12 + 6^2) % 13 = 9 → Insert at index 9
 
ii. If the hash table is designed to try up to 10 probes (i.e. up to h(x)+10^2), determine if there is a solution if you change the number 73 in the sequence to 74.
<br>Hash Values:
- h(77) = 77 % 13 = 12 → Insert at index 12
- h(94) = 94 % 13 = 3 → Insert at index 3
- h(74) = 74 % 13 = 9 → Insert at index 9
- h(90) = 90 % 13 = 12 → Collision at index 12
  - Probe 1: h(90, 1) = (12 + 1^2) % 13 = 13 % 13 = 0 → Insert at index 0
- h(55) = 55 % 13 = 3 → Collision at index 3
  - Probe 1: h(55, 1) = (3 + 1^2) % 13 = 4 → Insert at index 4
- h(51) = 51 % 13 = 12 → Collision at index 12
  - Probe 1: h(51, 1) = (12 + 1^2) % 13 = 0 → Collision at index 0
  - Probe 2: h(51, 2) = (12 + 2^2) % 13 = 8 → Insert at index 8
- h(54) = 54 % 13 = 2 → Insert at index 2
- h(76) = 76 % 13 = 11 → Insert at index 11
- h(103) = 103 % 13 = 12 → Collision at index 12
  - Probe 1: h(103, 1) = (12 + 1^2) % 13 = 0 → Collision at index 0
  - Probe 2: h(103, 2) = (12 + 2^2) % 13 = 8 → Collision at index 8
  - Probe 3: h(103, 3) = (12 + 3^2) % 13 = 5 → Insert at index 5

<br>Table after insertion:
- Index 0: [90]
- Index 1: []
- Index 2: [54]
- Index 3: [94]
- Index 4: [55]
- Index 5: [103]
- Index 6: []
- Index 7: []
- Index 8: [51]
- Index 9: [74]
- Index 10: []
- Index 11: [76]
- Index 12: [77]

<br>b. Using **Doubling Hashing** with a hash table of **size 13**, a hash function **h(x)=x mod 13**, an incremental hash function of **g(x)=(x mod 7) +1**,
<br>i. Show the contents of the hash table after inserting the following sequence of values: 77, 94, 73, 90, 55, 51, 54
<br>Hash Values:
- h(77) = 77 % 13 = 12 → Insert at index 12
- h(94) = 94 % 13 = 3 → Insert at index 3
- h(73) = 73 % 13 = 8 → Insert at index 8
- h(90) = 90 % 13 = 12 → Collision at index 12
  - g(90) = (90 mod 7) + 1 = 6+1 = 7
  - Probe i = 1: (12 + 1*7) mod 13 = (12+7) mod 13 = 6 → Insert at index 6
- h(55) = 55 % 13 = 3 → Collision at index 3
  - g(55) = (55 mod 7) + 1 = 6+1 = 7
  - Probe i = 1: (3 + 1*7) mod 13 = (3+7) mod 13 = 10 → Insert at index 10
- h(51) = 51 % 13 = 12 → Collision at index 12
  - g(51) = (51 mod 7) + 1 = 2+1 = 3
  - Probe i = 1: (12 + 1*3) mod 13 = (12+3) mod 13 = 2 → Insert at index 2
- h(54) = 54 % 13 = 2 → Collision at index 2
  - g(54) = 54 mod 7 + 1 = 5+1 = 6
  - Probe i = 1: (2 + 1*6) mod 13 = (2+6) mod 13 = 8 → Collision at index 8
  - Probe i = 2: (2 + 2*6) mod 13 = (2+12) mod 13 = 1 → Insert at index 1
