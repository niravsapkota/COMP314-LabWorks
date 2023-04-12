#Implementation of linear search and binary search

def linearSearch(values, target):
    n=len(values)
    for i in range(n):
        if values[i]==target:
            return i

    return -1


def binarySearch(values, low, high, target):
    if high>=low:
        mid=(high+low)//2

        if values[mid]==target:
            return mid

        elif values[mid] > target:
            return binarySearch(values, low, mid-1, target)

        else:
            return binarySearch(values, mid+1, high, target)
    else:
        return -1