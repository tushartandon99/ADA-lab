from typing import List, Tuple
import random


def findKthLargest(nums: List[int], k: int) -> int:
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid value of k")

    # Convert kth largest to index in sorted order
    target = len(nums) - k

    def quickselect(left, right):
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]

        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1

        nums[store], nums[right] = nums[right], nums[store]

        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    if not nums:
        raise ValueError("Array cannot be empty")

    minimum = maximum = nums[0]

    for num in nums[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


# Example
nums = [7, 10, 4, 3, 20, 15]

print("Kth Largest:", findKthLargest(nums.copy(), 3))
print("Min-Max:", findMinMax(nums))