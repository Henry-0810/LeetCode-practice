def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(nums[i])
            i -= 1
        i += 1
    return len(nums)


arr = [1, 2, 3, 4, 5, 6, 2, 2, 2]
print(removeElement(arr, 2))
