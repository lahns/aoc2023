def extrapolate(arr):
    if all(x == 0 for x in arr):
        return 0
    
    deltas = [y - x for x, y in zip(arr, arr[1:])]
    diff = extrapolate(deltas)
    return arr[-1] + diff

sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        nums = list(map(int, line.split()))[::-1] # for part two just reversed the nums array
        sum += extrapolate(nums)

print(sum)



