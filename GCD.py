# Greatest Common Divisor
n = int(input("n: "))
m = int(input("m: "))
 
for i in range(1, m+1):
    if (n%i == 0 and m%i == 0):
        gcd = i

print(gcd)