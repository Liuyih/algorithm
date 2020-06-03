#Yihong Liu

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

#open the input file
inputFile = open('data.txt', 'r')

#create the output file
outputFile = open('merge.out', 'w')
#convert the string to the array
array = inputFile.readline().split(' ')

while array != ['']:
    #change to the arrat of integers
    array = list(map(int,array))
    #discard the first number
    array = array[1:]
    #call the insertsort algorithm here
    output = mergesort(array)
    #write the result into the insert.out
    outputFile.write(' '.join(map(str,output)))
    outputFile.write('\n')
    #get a new line until it's empty, it will stop the while loop
    array = inputFile.readline().split(' ')

inputFile.close()
outputFile.close()
