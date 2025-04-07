def bubble_sort(arr):
    # Taken from here: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
    
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                temp1 = arr[i + 1]
                temp2 = arr[i]
                arr[i] = temp1
                arr[i + 1] = temp2
                swapped = True
        
        if not swapped:
            break

    return arr
    