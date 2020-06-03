import math
import random
from time import time
from fractions import Fraction


# Creates list of n random integers
def random_list(n):
    return [random.randint(0, 10000) for i in range(n)]


data_10 = random_list(10)
data_20 = random_list(20)
data_30 = random_list(30)
data_40 = random_list(40)
data_50 = random_list(50)
data_60 = random_list(60)
data_70 = random_list(70)


def badSort(arr, start, end, alpha):
    #size of the array
    if end - start == 1 and arr[end] < arr[start]:
        arr[start], arr[end] = arr[end], arr[start]
    elif end - start > 1:
        m = int(math.ceil(alpha * (end - start + 1)))
        #the way I fix it, to avoid infinite loop
        if m == end-start+1 :
            m = m-1
        badSort(arr, start, start + m - 1, alpha)
        badSort(arr, end - m + 1, end, alpha)
        badSort(arr, start, start + m - 1, alpha)

if __name__ == "__main__":
    # Get alpha value from user
    print("Please enter a fraction or decimal value for alpha < 1: ")
    alpha = float(Fraction(input()))
    print("Size       Running time")
    start_time_10 = time()
    badSort(data_10, 0, 9, alpha)
    elapsed_time_10 = time() - start_time_10
    print( " {}        {} ".format(10,elapsed_time_10))

    start_time_20 = time()
    badSort(data_20, 0, 19, alpha)
    elapsed_time_20 = time() - start_time_20
    print( " {}        {} ".format(20,elapsed_time_20))

    start_time_30 = time()
    badSort(data_30, 0, 29, alpha)
    elapsed_time_30 = time() - start_time_30
    print( " {}        {} ".format(30,elapsed_time_30))

    start_time_40 = time()
    badSort(data_40, 0, 39, alpha)
    elapsed_time_40 = time() - start_time_40
    print( " {}        {} ".format(40,elapsed_time_40))

    start_time_50 = time()
    badSort(data_50, 0, 49, alpha)
    elapsed_time_50 = time() - start_time_50
    print( " {}        {} ".format(50,elapsed_time_50))

    start_time_60 = time()
    badSort(data_60, 0, 59, alpha)
    elapsed_time_60 = time() - start_time_60
    print( " {}        {} ".format(60,elapsed_time_60))

    start_time_70 = time()
    badSort(data_70, 0, 69, alpha)
    elapsed_time_70 = time() - start_time_70
    print( " {}        {} ".format(70,elapsed_time_70))
