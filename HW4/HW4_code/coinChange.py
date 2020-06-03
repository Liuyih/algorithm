def find_min(N, denomination):
    n = len(denomination)
    # initializing the array
    ans = []
    # traversing through all the elements
    i = n - 1
    while i >= 0:
        # Finding denominations
        # dividing by maximum times a single element can come
        while N >= denomination[i]:
            N -= denomination[i]
            ans.append(denomination[i])
        i -= 1
    return ans


def find_denomination(c, k):
    # initializing the array
    denomination = []
    # ( c^0, c^1 ..... c^k )
    for i in range(k + 1):
        denomination.append(c ** i)
    # returning the array
    return denomination


def change():
    # reading from the data.txt
    file = open("data.txt", 'r')
    # to store in file
    outputFile = open ("change.txt" ,'w')
    lines = file.readlines()

    # reading data line by line
    for line in lines:
        # splitting the value
        val = line.strip().split(" ")
        # creating the denomination array
        denomination = find_denomination(int(val[0]), int(val[1]))
        # finding the change using greedy approach and saving in file

        # counting the frequency and storing in dictionary 
        change_denomination = count_frequency(find_min(int(val[2]), denomination))

        for key, value in change_denomination.items():
            # saving the key value pair in file
            outputFile.write(str("% d  % d" % (key, value)) + "\n")
        outputFile.write("\n")

    # closing the file after saving the result
    outputFile.close()


def count_frequency(denomination):
    # Creating an empty dictionary  
    frequency = {}
    for item in denomination:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
