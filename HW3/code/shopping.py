#basic knapsack algorithm but with adjusted parameters
def knapsack(W, P, N, M, table):
    K = [[0 for x in range(M + 1)] for x in range(N + 1)]

    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif W[i - 1] <= j:
                K[i][j] = max(P[i - 1] + K[i - 1][j - W[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    result = K[N][M]
    weight = M

    # Add items to the table
    for q in range(N, 0, -1):
        if result <= 0:
            break
        elif result > 0 and result == K[q - 1][weight]:
            continue
        else:
            table.append(q)
            result -= P[q - 1]
            weight -= W[q - 1]

    return K[N][M]


if __name__ == "__main__":
#initialize all the variables and files.
    input_file = open("shopping.txt")
    output_file = open ("result.txt" ,"w")
    test_cases = 0
    items = 0
    family_members = 0
    max_weight = 0
   
    # Get the number of test  cases from first line using readline 
    test_cases = int(input_file.readline())
    
    # initialize price and weight array
    for test in range(test_cases):
        prices = []
        weights = []
        
        #print("Test Case " + str(test + 1))
        output_file.write("Test Case {}".format(str(test + 1)))
        output_file.write('\n')
        items = int(input_file.readline())

        # For each item, get its weight and price
        for item in range(items):
            item_attributes = input_file.readline().split(' ')
            # the first one is price
            prices.append(int(item_attributes[0]))
            # the second one is weight
            weights.append(int(item_attributes[1]))

        # Initialize the current maximum calculated price to 0
        maxPrice = 0

        # Get the total number of family members
        family_members = int(input_file.readline())

        data_table = [[] for i in range(family_members)]

        # Get the maximum value that can be carried by each family member
        for member in range(family_members):
            max_weight = int(input_file.readline())
            maxPrice = knapsack(weights, prices, items, max_weight, data_table[member]) + maxPrice

        for element in data_table:
            element.sort()

        #print ("Total Price " + str(maxPrice))
        output_file.write("Total Price {}".format(str(maxPrice)))
        output_file.write('\n')
        #print("Member Items")
        output_file.write("Member Items")
        output_file.write('\n')
        for member in range(family_members):
            #print(str(member + 1) + ": ")
            output_file.write(str(member + 1) + ": ")
            
            for item in data_table[member]:
                #print(item)
                output_file.write("\t{}".format(str(item)))
            output_file.write('\n')
            output_file.write('\n')
            #print('\n')
    output_file.close()

