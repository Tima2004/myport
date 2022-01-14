def Series(n):
    sums = 0
    for i in range(1, n + 1):
        sums += (i * i);
    return sums

# Driver Code
n = 5
res = Series(n)
print(res)

def getSum(n):

    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    return sum


# Driver code
n = 123
print(getSum(n))

a = 'aman tima ammm'
b = a.title()
print(b)
