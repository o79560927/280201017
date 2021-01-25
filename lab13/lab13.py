def selection_sort(liste):
    for i in range(len(liste)):
        min_index = i
        for k in range(i + 1, len(liste)):
            if liste[k] < liste[min_index]:
                min_index = k
        (liste[i], liste[min_index]) = (liste[min_index], liste[i])


numbers = [16, 342, 343, 2, 34]
selection_sort(numbers)
print(numbers)



def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10
# Function call
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
