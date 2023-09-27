def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # quick method but time complexity not optimum O((m+n)log(m+n))
    """
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()
    """
    nums1[m:] = [0] * (n)

    p1 = m - 1
    p2 = n - 1

    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    if p2 >= 0:
        nums1[: p2 + 1] = nums2[: p2 + 1]


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
print(" ".join(map(str, nums1)))
