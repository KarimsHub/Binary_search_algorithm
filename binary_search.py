def binary_search(sorted_list, number):
    first = 0 # first element in list (1)
    last = len(sorted_list) -1 # get the last element in the list (13370)
    found = False

    while(found == False and first <= last):
        mid = (first + last) // 2 # gets the middle index number of items in the list (in this case it's index 5)
        if sorted_list[mid] == number: # checks if the item on index 5 is the same as the number we're searching for
            found = True
            return mid
        else:
            if number > sorted_list[mid]:
                first = mid + 1 # setting the start of the list right after the mid to look in the right part of the list
            else:
                last = mid - 1 # setting the end of the list right before the midpoint to shorten the list and look at the left part
    
    return found





l = [1, 2, 4, 8, 9, 42, 1337, 1338, 5600, 13370]

print(binary_search(l, 1337))

