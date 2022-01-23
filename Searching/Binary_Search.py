def binarySearchIterative(arr, target):
    # time complexity: O(log(n))
    # space complexity: O(1)

    start = 0 # Start index
    end = len(arr) - 1 # End index
    while start <= end: # While start index is less than or equal to end index
        mid = (start + end) // 2 # Find mid
        if arr[mid] == target: # Found
            return mid
        elif arr[mid] < target: # Search right
            start = mid + 1
        else: # Search left
            end = mid - 1
    return -1 # Not found

def binarySeachRecursice(arr, target, low=0, high=0):
    # time complexity: O(log(n))
    # space complexity: O(log(n))
    
    if low > high: # Base case
        return -1 # Not found
    mid = (low + high) // 2 # Find mid
    if arr[mid] == target: # Found
        return mid
    elif arr[mid] < target: # Search right
        return binarySeachRecursice(arr, target, mid + 1, high) # Recursive call on the right half
    else: # Search left
        return binarySeachRecursice(arr, target, low, mid - 1) # Recursive call on the left half

if __name__ == "__main__":
    # driver code
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearchIterative(arr, 5))
    print(binarySearchIterative(arr, 15))
    print(binarySeachRecursice(arr, 5))
    print(binarySeachRecursice(arr, 15))