from random import randint

#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a

#sorts list of random numbers
def cocktailSort(c):
    n = len(c) +1
    t = -1
    loop = True
    counter = 0
    while loop == True:
        inOrder = True
        counter += 1
        n -= 1
        t += 1
        for i in range(t, n): #bubble sorts forward
            if i + 1 < n:
                if c[i + 1] < c[i]: #compares values
                    c[i + 1], c[i] = c[i], c[i + 1] #swaps numbers
                    inOrder = False
                    
                print(c)
                print("Forwards")
                print()
            
        for i in range(n, t, -1):#bubble sorts backwards
            if i - 1 >= 0 and i < n:
                if c[i - 1] > c[i]: #compares values
                    c[i - 1], c[i] = c[i], c[i - 1] #swaps numbers
                    inOrder = False
                    
                print(c)
                print("Backwards")
                print()
            
            
        if inOrder == True:# ends while loop if sorted
            loop = False

    return c, counter

b = test()
print("Original: " + str(b))
d = cocktailSort(b)
print()
print("Sorted: " + str(d[0]))
print("Output: " + str(d[1]))

