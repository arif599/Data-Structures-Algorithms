def stringSubsetsPrint(string, subset=""):
    # base case
    if len(string) == 0:
        if subset == "":
            return 
            
        print(subset)
        return
    
    # recursive case
    stringSubsetsPrint(string[1:], subset+string[0]) # consider the first character
    stringSubsetsPrint(string[1:], subset) # don't consider the first character

def stringSubsetsArray(string, subset="", result=[]):
    # base case
    if len(string) == 0:
        if subset == "":
            return 

        result.append(subset)
        return

    # recursive case
    stringSubsetsArray(string[1:], subset+string[0], result) # consider the first character
    stringSubsetsArray(string[1:], subset, result) # don't consider the first character
    return result

def stringSubsetsArray2(string, subset=""):
    # base case
    if len(string) == 0:
        if subset == "":
            return []

        return [subset]

    # recursive case
    left = stringSubsetsArray2(string[1:], subset+string[0]) # consider the first character
    right = stringSubsetsArray2(string[1:], subset) # don't consider the first character
    
    return left+right

if __name__ == "__main__":
    stringSubsetsPrint("abc")
    print(stringSubsetsArray("abc"))
    print(stringSubsetsArray2("abc"))