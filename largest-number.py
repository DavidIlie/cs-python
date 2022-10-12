numbers = []

num_of_numbers = int(
    input("please input how many numbers you'd like to use. "))

for i in range(num_of_numbers):
    option = int(input("input #" + str(i + 1) + ". "))
    numbers.append(option)

# numbers.sort(reverse=True)
numbers.sort()

print(numbers)