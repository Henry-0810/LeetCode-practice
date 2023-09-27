import unittest


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


arr = [1, 1, 2]
print(removeDuplicates(arr))
# class TestRemoveDuplcates(unittest.TestCase):
#     # Test Case 1
#     def testNoDuplicate(self):
#         arr = [1, 2, 3, 4, 5]
#         expected_result = [1, 2, 3, 4, 5]
#         self.assertEqual(removeDuplicates(arr), expected_result)

#     def testDuplicates(self):
#         arr = [1, 1, 2]
#         expected_result = [1, 2]
#         self.assertEqual(removeDuplicates(arr), expected_result)

#     def testZeros(self):
#         arr = []
#         expected_result = []
#         self.assertEqual(removeDuplicates(arr), expected_result)


# if __name__ == "__main__":
#     unittest.main()
