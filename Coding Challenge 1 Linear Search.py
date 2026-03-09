def linear_search(numbers, target):
    # Loop through each index in the list
    for i in range(len(numbers)):
        # Check if the current number matches the target
        if numbers[i] == target:
            return i  # Return the index where the target was found
    return -1  # Return -1 if the target is not in the list

nums = [4, 7, 1, 9, 3]
target = 4

result = linear_search(nums, target)

print(result + 1) 