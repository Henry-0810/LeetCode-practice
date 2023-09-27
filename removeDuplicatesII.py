def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j, duplicate = 0, 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicate += 1
            if duplicate > 2:
                nums.remove()
                duplicate = 0
        j += 1

    return len(nums)


arr = [1, 2, 2, 2, 3, 3]
print(removeDuplicates(arr))
