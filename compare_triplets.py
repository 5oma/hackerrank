#Compare the Triplets
a = [17, 28, 30]
b = [99, 16, 8]

def compareTriplets(a, b):
    #initializing
    alice = 0
    bob = 0
    #logic
    if a[0] > b[0]:
        alice = alice + 1
    elif a[1] > b[1]:
        alice = alice + 1
    elif a[2] > b[2]:
        alice = alice + 1
    elif a[0] < b[0]:
        bob = bob + 1
    elif a[1] < b[1]:
        bob = bob + 1
    elif a[2] < b[2]:
        bob = bob + 1
    return(alice, bob)
        