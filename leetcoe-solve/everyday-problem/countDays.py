from typing import List


class Solution:
  """
  @title:3169. 无需开会的工作日
  @link: https://leetcode.cn/problems/count-days-without-meetings/?envType=daily-question&envId=2025-07-11
  @tag: 区间合并
  """

  def countDays(self, days: int, meetings: List[List[int]]) -> int:

    meetings.sort(key=lambda x: x[0])
    ans = meetings[0][0] - 1
    end = meetings[0][1]
    for s, e in meetings[1:]:
      if not end >= s:
        ans += s - end - 1
      end = max(end, e)
    #    print(f"s: {s}, e: {e},end = {end}, ans = {ans}")
    ans += days - end
    return ans;
