from random import randint
from time import time

MIN_INT = 0
MAX_INT = 10000

def merge(left,right):
    #create empty array to hold sorted values
    array = []
    #keep merge until one side has no element left
    while len(left) != 0 and len(right) != 0:
        #if the first element of left array is smaller merge it into empty array
        #and remove the merged element
        if left[0] < right[0]:
            array.append(left[0])
            left.remove(left[0])
        # the situation that is equal or bigger than right side
        else:
            array.append(right[0])
            right.remove(right[0])
    #if the left side array is empty, then append the right side
    if len(left) == 0:
        array += right;
    else:
        array += left;
    return array
#define mergesort algorithm
def mergesort(array):
    array_size = len(array)

    if array_size <= 1:
        return array
    else:
        array_split = array_size//2
        left_array = mergesort(array[:array_split])
        right_array = mergesort(array[array_split:])
        return merge(left_array,right_array)

if __name__ == "__main__":
    begin = 10000
    increment = 5000
    values = [begin + i * increment for i in range(7)]
    list   = [[randint(MIN_INT,MAX_INT) for _ in range(value)] for value in values]

    print ("value           running time")

    for array in list:
        array_size = len(array)

        start_time = time()

        mergesort(array)

        print("{}           {}".format(array_size,time()-start_time))
