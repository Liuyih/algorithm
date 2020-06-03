from random import randint
from time import time

MIN_INT = 0
MAX_INT = 10000

def insertsort(array):
    #go through each element in the array
    for j in range (1,len(array)):
        key = array[j];
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i -1
        array[i+1] = key
    return array

if __name__ == "__main__":
    begin = 10000
    increment = 5000
    values = [begin + i * increment for i in range(7)]
    list   = [[randint(MIN_INT,MAX_INT) for _ in range(value)] for value in values]

    print ("value           running time")

    for array in list:
        array_size = len(array)

        start_time = time()

        insertsort(array)

        print("{}           {}".format(array_size,time()-start_time))
