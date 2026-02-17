def search(arr,x):
    n = len(arr)
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr = [10,20,30,40,50,60,70,80]
    x = 60
    result = search(arr,x)
    if (result == -1):
        print("The element is not present in array")
    else:
        print("The element is present in array at index:", result)
