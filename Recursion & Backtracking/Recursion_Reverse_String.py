# time complexity: O(n) and space complexity: O(n)
def reverseString(str, n):
    if n == 0:
        print(str[n])
        return

    print(str[n], end="")
    reverseString(str, n-1)

if __name__ == "__main__":
    str = "abcde"
    n = len(str)-1
    reverseString(str, n)
    