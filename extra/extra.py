def isJump(n):
        if n <= 10: #if n < 10, it's always true
            return True

        n = list(str(n))
        for i in range(1, len(n)):
            diff = abs(int(n[i]) - int(n[i-1]))

            if diff !=1:
                return False

        return True


number = int(input("Enter a number:"))
for i in range(number):
    if (isJump(i)): #if isJump is true, print out the number 'i' itself.
        print(i,end=" ")
