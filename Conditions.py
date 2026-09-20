age = int(input())
if age >= 18: 
    print("Eligible for voting")
elif age >= 13:
    print("Teen")
else:
    print("Child")
n = int(input())
result = "Even" if n % 2 == 0 else "Odd"
print(result)