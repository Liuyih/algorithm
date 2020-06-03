#Yihong Liu

# insertion sort algorithm
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

#open the input file
inputFile = open('data.txt', 'r')

#create the output file
outputFile = open('insert.out', 'w')
#convert the string to the array
array = inputFile.readline().split(' ')

while array != ['']:
    #change to the arrat of integers
    array = list(map(int,array))
    #discard the first number
    array = array[1:]
    #call the insertsort algorithm here
    output = insertsort(array)
    #write the result into the insert.out
    outputFile.write(' '.join(map(str,output)))
    outputFile.write('\n')
    #get a new line until it's empty, it will stop the while loop
    array = inputFile.readline().split(' ')

inputFile.close()
outputFile.close()
