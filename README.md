# LeetCode
My notes and solution for leetcode problems.

## 常用文档
#### Python 包
[collections](https://docs.python.org/3/library/collections.html#counter-objects), 
[heapq](https://docs.python.org/3/library/heapq.html)
## DFS

#### [526. Beautiful Arrangement (similar to 46)](https://leetcode.com/problems/beautiful-arrangement/), [Solution](DFS/Beautiful_Arrangement.py)
T(N!), O(N)

直接backtrack，用一个self.count来记录当前有效permutation。每次idx到末尾就更新count。
#### [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/), [Solution](/DFS/Partition_to_K_Equal_Sum_Subsets.py)
T($k*2^N$), O(N)

先检测整体和是否能被k整除，可以的话用backtrack。每次往当前和里加一个元素，如果超过target_sum就直接返回，如果等于就count += 1然后当前和清零继续下一次backtrack，如果小于就依次往当前和里加入下一个元素并backtrack。注意就算从当前元素，不从头开始backtrack，且预先排序，依然在python上超时。


  
  ***
### 记忆化搜索（DFS + Memoization Search）：算是动态规划的一种，递归每次返回时同时记录下已访问过的节点特征，避免重复访问同一个节点，可以有效的把指数级别的DFS时间复杂度降为多项式级别; 注意这一类的DFS必须在最后有返回值，不可以用排列组合类型的DFS方法写; for循环的dp题目都可以用记忆化搜索的方式写，但是不是所有的记忆化搜索题目都可以用for循环的dp方式写。

#### [139. Word Break](https://leetcode.com/problems/word-break/), [Solution](DFS/Word_Break.py)
用backtrack往下一个个查，注意要缓存不然会超时。用`@lru_cache`缓存。
#### [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/), [Solution](DFS/Longest_Increasing_Path_in_a_Matrix.py)
dfs返回从当前坐标开始的最长路径长度，用一个path_length来记录已计算过的格子

#### [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/description/), [Solution](DFS/Concatenated_Words.py)
直接dfs，对每个单词从每个下标分成两半，查找前一半和后一半是否在words里或者能表示成words里词的拼接。把words转换成set，加上memorization来提速。

1235 Maximum Profit in Job Scheduling
1335 Minimum Difficulty of a Job Schedule

## Heap

#### [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/), [Solution](Heap/Find_Median_from_Data_Stream.py)
建一个最大堆和一个最小堆，保存他们的大小，每次有新的数进来就让他进最小或最大堆，保持最大堆和最小堆个数相等或者多1。

## DP

#### [72. Edit Distance](https://leetcode.com/problems/edit-distance/), [Solution](DP/Edit_Distance.py)

明明是DP不是DFS啊。如果作change，看看当前位置的character是否一样。如果作delete，在dp[i-1][j]上加1。如果作insert，在dp[i][j-1]上加1。取三个里面最小的。

#### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/description/), [Solution](DP/Interleaving_String.py)
用的算是brute force+cache，但其实可以用DP。dp[i][j]储存能否用s1[:i+1]和s2[:j+1]interleave出s3[:i+j+1]。

#### [Contest 315 No.4 Count Subarrays With Fixed Bounds](https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/), [Solution](DP/Count_Subarrays_With_Fixed_Bounds.py)
先过一遍nums，记录每个坐标前最近的等于minK，等于maxK，超出范围的值的坐标，记为prev[0], prev[1], prev[2]。然后dp。dp[i] = dp[i-1]，如果nums[i]没超出范围，那么dp[i]再加上prev[0], prev[1]里更小的那个到prev[2]的距离。如果是负的就不加。

#### [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/),[Solution](DP/Combination_Sum_IV.py)
对target进行dp，以nums里的每个数num作结尾都是不同的组合，然后dp(target-num)。用cache加记忆。

#### [403. Frog Jump](https://leetcode.com/problems/frog-jump/description/), [Solution](DP/Frog_Jump.py)
不是最优解，差不多是brute force+cache。可以用DP。用一个字典储存key:value, key是每个位置，value是能到这个位置的jump的长度的集合。最后如果最后一个位置在字典里，就说明可以跳到这里，否则不可以。

#### [1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/description/), [Solution](DP/Valid_Palindrome_III.py)
直接dp，能不能变成palindrome取决于变成palindrome的最小次数是否小于k。dfs(i, j)如果s的i和j相等，则等于dfs(i+1, j-1)。否则说明i或者j之间要去掉一个，就等于1+min(dfs(i+1, j), dfs(i, j-1))。