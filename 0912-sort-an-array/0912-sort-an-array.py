import random
class Solution:
    def sortArray(self, nums):
        def quicksort(left, right):
            while left < right:
                pivot_index = random.randint(left, right)
                pivot = nums[pivot_index]
                i = left
                j = left
                k = right
                while j <= k:
                    if nums[j] < pivot:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j += 1
                    elif nums[j] > pivot:
                        nums[j], nums[k] = nums[k], nums[j]
                        k -= 1
                    else:
                        j += 1

                if i - left < right - k:
                    quicksort(left, i - 1)
                    left = k + 1
                else:
                    quicksort(k + 1, right)
                    right = i - 1
        quicksort(0, len(nums) - 1)
        return nums