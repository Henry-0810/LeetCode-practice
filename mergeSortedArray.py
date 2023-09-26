from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, count1, count2 = 0, 0, 0
    while i < (m + n):
        if nums1[count1] > nums2[count2] and count1 < m and count2 < n:
            temp = nums1[count1]
            nums1[count1] = nums2[count2]
            nums1[count1] = temp
            count2 += 1
        else:
            count1 += 1
        i += 1


nums1 = [1, 2, 3]
nums2 = [3, 4, 5]
merge(nums1, len(nums1), nums2, len(nums2))
print(nums1)
