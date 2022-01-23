def binarySearchIterative(arr, val):
    start = 0 # Start index
    end = len(arr) - 1 # End index
    while start <= end: # While start index is less than or equal to end index
        mid = (start + end) // 2 # Find mid
        if arr[mid] == val: # Found
            return mid
        elif arr[mid] < val: # Search right
            start = mid + 1
        else: # Search left
            end = mid - 1
    return -1 # Not found

def binarySeachRecursice(arr, val, low=0, high=0):
    if low > high: # Base case
        return -1 # Not found
    mid = (low + high) // 2 # Find mid
    if arr[mid] == val: # Found
        return mid
    elif arr[mid] < val: # Search right
        return binarySeachRecursice(arr, val, mid + 1, high) # Recursive call on the right half
    else: # Search left
        return binarySeachRecursice(arr, val, low, mid - 1) # Recursive call on the left half

if __name__ == "__main__":
    # driver code
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearchIterative(arr, 5))
    print(binarySearchIterative(arr, 15))
    print(binarySeachRecursice(arr, 5))
    print(binarySeachRecursice(arr, 15))