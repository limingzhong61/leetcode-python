from collections import Counter
from typing import List

# everyday-problem: #1865
# https://leetcode.cn/problems/finding-pairs-with-a-certain-sum/description/?envType=daily-question&envId=2025-07-06
class FindSumPairs:

  def __init__(self, nums1: List[int], nums2: List[int]):
    self.map = {}
    self.nums2 = nums2
    self.nums1 = nums1
    self.cnt = Counter(nums2)

  def add(self, index: int, val: int) -> None:
    # 维护 nums2 每个元素的出现次数
    self.cnt[self.nums2[index]] -= 1
    self.nums2[index] += val
    self.cnt[self.nums2[index]] += 1

  def count(self, tot: int) -> int:
    ans = 0
    for x in self.nums1:
      ans += self.cnt[tot - x]
    return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
