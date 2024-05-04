numbers = input()
k = input()

for i in range(len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers.pop()

print(numbers)
