
import math
from fractions import Fraction

list_data = []

input_file = open("data.txt")
# Convert input from data.txt to integers into a list
for line in input_file:
    list_data.append([int(x) for x in line.split() if x.isdigit()])
#remove the first number of each line, can also use pop or slice
for line in list_data:
    line.remove(line[0])


#implement the sudocode in here
def bad_sort(arr, start, end, alpha):
    #size of the array
    if end - start == 1 and arr[end] < arr[start]:
        arr[start], arr[end] = arr[end], arr[start]
    elif end - start > 1:
        m = int(math.ceil(alpha * (end - start + 1)))
        #the way I fix it, to avoid infinite loop
        if m == end-start+1 :
            m = m-1
        bad_sort(arr, start, start + m - 1, alpha)
        bad_sort(arr, end - m + 1, end, alpha)
        bad_sort(arr, start, start + m - 1, alpha)


if __name__ == '__main__':

    print("Please enter a fraction or decimal value for alpha < 1: ")
    alpha = float(Fraction(input()))
    for element in list_data:
        length = len(element)
        bad_sort(element, 0, length - 1, alpha)

    with open("bad.out", "w") as output_file:
        for line in list_data:
            output_file.write("%s\n" % line)
