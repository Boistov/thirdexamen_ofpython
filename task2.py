numbers = [int(x) for x in input().split()]

count = 1
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        count += 1

# Output
print(count)
