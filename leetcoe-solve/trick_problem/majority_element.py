from typing import List


class Solution:
  """
  @title: 169. 多数元素
  @link: https://leetcode.cn/problems/majority-element/description/?envType=study-plan-v2&envId=top-100-liked
  @tag: Boyer-Moore 投票算法
  @description: 如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
  """
  def majorityElement(self, nums: List[int]) -> int:
    value, cnt = 0, 0
    for num in nums:
      if value == num:
        cnt += 1
      else:
        if cnt > 0:
          cnt -= 1
        else:
          cnt = 1
          value = num
    return value

class Solution2:
  """
  @description: official solution
  """
  def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
      if count == 0:
        candidate = num
      count += (1 if num == candidate else -1)

    return candidate
