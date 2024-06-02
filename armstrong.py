
arr=[]
sum =0
def getDigits(num):
    s=str(num)
    for i in s:
        arr.append(int(i))
    
a =int(input("Enter the number"))
getDigits(a)

for i in arr:
    sum = sum + i**3
    
if sum == a :
    print("Is Armstrong number")
else:
    print("Not armstrong number")