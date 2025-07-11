from typing import List


class Solution:
  """
  @name: 35. 搜索插入位置
  @link: https://leetcode.cn/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-100-liked
  @type: binary search
  """

  def searchInsert(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
      mid = (low + high) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        high = mid - 1
      else:
        low = mid + 1
    return low
