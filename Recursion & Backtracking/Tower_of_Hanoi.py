# Time complexity: O(2^n)
def TowerOfHanoi(n , source, helper, destination):
    # base case
    if n == 1: 
        print("Transfer disk 1 from source", source, "to destination", destination) # move disk 1 (largest disk) from source A to destination C
        return
    
    # recursive case
    TowerOfHanoi(n-1, source, destination, helper) # move n-1 disks from source A to helper B
    print("Transfer disk", n,"from source", source,"to destination", destination)
    TowerOfHanoi(n-1, helper, source, destination) # move n-1 disks from helper B to destination C
          
if __name__ == "__main__":
    n = 4
    TowerOfHanoi(n, "S", "H", "D") 

