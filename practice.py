import math


def swap(arr,i,j):

    x = arr[i]
    y = arr[j]
    arr[i] = y
    arr[j] = x

def maxHeap(arr):

    counter = len(arr)//2 - 1
    checker = 0

    while checker < len(arr)//2:

        if counter == len(arr)//2 - 1:
            if 2*counter + 2 == len(arr) -1:
                if arr[2*counter + 2] > arr[counter]:
                    swap(arr,2*counter + 2,counter)
        elif arr[2*counter + 2] > arr[counter]:
                    swap(arr,2*counter + 2,counter)

        if arr[2*counter + 1] > arr[counter]:
            swap(arr,2*counter + 1, counter)

        else:
            checker +=1
        print(counter)
        print(arr)
        counter -= 1

        if counter < 0 and checker < len(arr)//2:
            counter = len(arr)//2 - 1
            checker = 0

arr = [1,3,6,5,9,8]


maxHeap(arr)






