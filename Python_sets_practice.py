print("QUESTION 1: Enter 5 names --> Show how many are unique")
names = set()
for _ in range(5):
    names.add(input("Enter name:"))
print("Unique:" , names)
print("Total unique:", len(names))

print("QUESTION 2: Keep entering numbers till -1 --> Print sum of unique numbers")
nums = set()
while True:
    n =int(input("Enter number (-1 to stop): "))
    if n == -1:
        break
    nums.add(n)

print("Unique numbers:", nums)
print("Sum: ", sum(nums))