# Binary search Algorithm

Binary search looks for a particular item by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. This process continues on the sub-array as well until the size of the subarray reduces to zero.


## Working of this algorithm:
- For a binary search to work, it is mandatory for the target array to be sorted.
- Binary search halves the searchable items and thus reduces the count of comparisons to be made to very less numbers.


## Complexity:
- Binary search is a fast search algorithm with run-time complexity of Ο(log n)
- O(log n) is much faster than O(n) and really efficient


## Advantages of Binary search:

- Compared to linear search (checking each element in the array starting from the first), binary search is much faster. Linear search takes, on average N/2 comparisons (where N is the number of elements in the array), and worst case N comparisons. Binary search takes an average and worst-case  𝑙𝑜𝑔2(𝑁)  comparisons. So for a million elements, linear search would take an average of 500,000 comparisons, whereas binary search would take 20.
- It’s a fairly simple algorithm

## Disadvantages of Binary search:

- It’s more complicated than linear search, and is overkill for very small numbers of elements.
- It works only on lists that are sorted and kept sorted. That is not always feasable, especially if elements are constantly being added to the list.
- There is a great lost of efficiency if the list does not support random-access. You need, for example, to immediately jump to the middle of the list. If your list is a plain array, that’s great. If it’s a linked-list, not so much.

![ImgName](https://github.com/KarimsHub/Binary_search_algorithm/blob/master/binary-search.jpg?raw=true)
