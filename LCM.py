a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

x= lcm(a,b)

print(x)