# LeetCode
My notes and solution for leetcode problems.

## 目录

<ol>
  <li> <a href=#常用文档>常用文档</a></li>
  <li> <a href=#String>String</a></li> 
  <li> <a href=#List>List</a></li> 
  <li> <a href=#Hashmap>Hashmap</a></li> 
  <li> <a href=#LinkedList>Linked List</a></li> 
  <li> <a href=#Tree>Tree</a></li> 
  <li> <a href=#Heap>Heap</a></li> 
  <li> <a href=#Sort>Sort</a></li> 
  <li> <a href=#SlidingWindow>SlidingWindow</a></li> 
  <li> <a href=#DFS>DFS</a></li> 
  <li> <a href=#BFS>BFS</a></li> 
  <li> <a href=#DP>DP</a></li> 
  <li> <a href=#OOD>OOD</a></li> 
</ol>

<div id='常用文档'></div>

## 常用文档
#### Python 包
[collections](https://docs.python.org/3/library/collections.html#counter-objects), 
[heapq](https://docs.python.org/3/library/heapq.html), [itertools](https://docs.python.org/3/library/itertools.html), [bisect](https://docs.python.org/3/library/bisect.html)

---

<div id='String'></div>

## String

#### [2268. Minimum Number of Keypresses](https://leetcode.com/problems/minimum-number-of-keypresses/description/), [Solution](String/Minimum_Number_of_Keypresses.py)
直接过一遍str，让频率高的放在第一个，9个button放完了就放第二个，依次。每放一个字母就count += number of ch in str * 字母在button里的位置。

#### [2288. Apply Discount to Prices](https://leetcode.com/problems/apply-discount-to-prices/description/), [Solution](String/Apply_Discount_to_Prices.py)
简单，不过注意字符串里插入变量的格式：'str%格式'%(插入的东西)

---

<div id='List'></div>

## List

#### [163. Missing Ranges](https://leetcode.com/problems/missing-ranges/description/), [Solution](List/Missing_Ranges.py)
直接过一遍nums，如果和前一个相差大于一则ans.append一个数或一个区间。注意corner case，比如nums = []，以及lower和upper处的情况。

#### [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/description/), [Solution](List/Meeting_Rooms.py)
直接过一遍，检查每个meeting的开始时间是否早于前一个的结束时间。

#### [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/), [Solution](List/Minimum_Moves_to_Equal_Array_Elements.py)
其实很简单。要想到增加n-1个数等价于减少1个数。然后算每个数跟最小值的差就行了。

#### [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/), [Solution](List/Degree_of_an_Array.py)
先过一遍，用字典记录每个数字的频率，第一次和最后一次出现的位置。再过一遍字典，更新max_fre和min_len。

#### [1864. Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/description/), [Solution](List/Minimum_Number_of_Swaps_to_Make_the_Binary_String_Alternating.py)
因为只有两个字母，所以只要算其中一个字母不在正确位置上的最小位置数就行了。取两个字母里面这个数更小的那一个。

#### [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/description/), [Solution](List/Angle_Between_Hands_of_a_Clock.py)
直接算出时针和秒针的角度，然后取差的绝对值，再取跟补角里更小的那个。

#### [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/), [Solution](List/Maximum_Difference_Between_Increasing_Elements.py)
easy，一个指针过一遍，比较当前元素和之前最小元素，更新当前最小元素。

#### [2214. Minimum Health to Beat Game](https://leetcode.com/problems/minimum-health-to-beat-game/description/), [Solution](List/Minimum_Health_to_Beat_Game.py)
直接求和然后减去armor和max(damage)里的最小值表示抵消一次攻击。完全是easy啊为什么会是medium。


#### [2221. Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/description/), [Solution](List/Find_Triangular_Sum_of_an_Array.py)
用Pascal Triangle即组合数来算每个数在最终答案里用到的次数，然后直接一个个加上去。注意算组合数的时候要用//不要用/，不然后面会小数位有问题。也可以直接recursive做，不过很慢。


#### [2294. Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/), [Solution](List/Partition%20Array%20Such_That_Maximum_Difference_Is_K.py)
直接排个序然后从小到大分就行。

#### [2357. Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/), [Solution](List/Make_Array_Zero_by_Subtracting_Equal_Amounts.py)
先排序，然后依次处理值不一样的元素，被减去的值等于max(nums)的时候就结束。

---

<div id='Hashmap'></div>

## Hashmap

#### [1. Two Sum](https://leetcode.com/problems/two-sum/description/), [Solution](Hashmap/Two_Sum.py)
用hashmap储存与当前值的和为target的值，以及当前值的index。继续查找每一个值，如果在hashmap里就输出储存的index和当前的index。

#### [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/), [Solution](Hashmap/Two_Sum_III_-_Data_structure_design.py)
跟Two Sum一样，不过把hashmap的值的index换成了count，因为只要找到是否有就行了不要下标。然后用count可以避免重复访问同一个元素。


#### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/), [Solution](Hashmap/Subarray_Sum_Equals_K.py)
用一个hashmap记录到每个下标为止的子串合对应的子串数。对每个新下标，count加上合为 当前子串合 - k 的子串数。

<div id='LinkedList'></div>

---

## Linked List
#### [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/), [Solution](LinkedList/Add_Two_Numbers.py)
创建一个新链表，如果l1或l2后面还有就继续延长这个链表

---

<div id='Tree'></div>

## Tree

#### [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/description/), [Solution](Tree/Boundary_of_Binary_Tree.py)
直接分别取left boundary, leaves, and right boundary。

#### [2471. Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/), [Solution](Tree/Minimum_Number_of_Operations_to_Sort_a_Binary_Tree_by_Level.py)
用两个queue按层bfs遍历树，然后对每层求min swap。重点是min swap。注意iterative traversal的时候就用普通stack就行，然后先后顺序反过来。

---

<div id='Heap'></div>

## Heap

#### [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/), [Solution](Heap/Meeting_Rooms_II.py)
Use a heap to keep the end time of each room. Process meetings by their start time. If the start time is earlier than the earliest endtime, then it means more room is needed. Otherwise just allocate the already finished room to the current meeting.
#### [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/), [Solution](Heap/Find_Median_from_Data_Stream.py)
建一个最大堆和一个最小堆，保存他们的大小，每次有新的数进来就让他进最小或最大堆，保持最大堆和最小堆个数相等或者多1。

#### [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/description/), [Solution](Heap/Meeting_Rooms_III.py)
用两个min heap，一个保存可以用的房间，一个保存使用中的房间，以结束时间为关健字。每一步先把结束时间小于当前开始时间的都挪到可用房间，如果当前有可用房间则直接用，没有的话则推迟当前meeting到下一个可以用的房间为止。

---

<div id='Sort'></div>

## Sort

#### [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2/problem), [Solution](Sort/Minimum_Swaps_2.py)
把数组看成一个图，每个数字是一个节点，从当前位置到排序好后应该在的位置有一条边，得到一些不交的圈。最后swap数 = sum(每个圈的大小 - 1)。按顺序遍历排序后的数组，用元组保存原始位置，通过访问原始位置来遍历整个圈。用一个list或者set来track是否每个元素都visit了。


#### [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/), [Solution](Sort/Find_K-th_Smallest_Pair_Distance.py)
比较复杂，对pair distance用binary search，用一个possible表示是否有k或更多个pair的distance小于等于v。用prefix sum来简化对possible的计算。直接抄的，之后重写一遍。


#### [937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/), [Solution](Sort/Reorder_Data_in_Log_Files.py)
自定义key排序，先找一遍把数字都找出来，剩下的分别按content和identifier排序。也可以统一一起排序，key为另一个还是，用来生成一个tuple产生顺序。注意str.split()可以定义maxsplit。


#### [1152. Analyze User Website Visit Pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/description/), [Solution](Sort/Analyze_User_Website_Visit_Pattern.py)
用一个dict记录每个人的访问顺序，然后用Counter记录每个人访问过的网站的所有combination，然后用max，key=lambda x:pattern[x]取出pattern里面最大且字典序最小的元素那个

#### [1356. Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/), [Solution](Sort/Sort_Integers_by_The_Number_of_1_Bits.py)
直接做。可以一行解决其实。注意python有bin函数，直接返回一个数的二进制表达。另外count函数直接返回一个数里某个数的个数。


#### [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/), [Solution](List/Maximum_Units_on_a_Truck.py)
简单的单位容量背包问题，直接按价值从大到小放就行了。

#### [2055. Plates Between Candles](https://leetcode.com/problems/plates-between-candles/description/), [Solution](Sort/Plates_Between_Candles.py)

记录下所有candle的位置，然后对每个query用二分，找到从左往右和从右往左的第一个candle，然后两个之间的距离减去两个之间的candle数，就是plate数。


#### [2340. Minimum Adjacent Swaps to Make a Valid Array](https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/), [Solution](Sort/Minimum_Adjacent_Swaps_to_Make_a_Valid_Array.py)
直接找到第一个最小元素和最后一个最大元素，然后算把他们放到正确位置的swap数。


---

<div id='SlidingWindow'></div>

## Sliding Window

#### [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/), [Solution](SlidingWindow/Sliding_Window_Maximum.py)
要想到maintain一个deque，储存当前window里从最大元素开始往右依次减小的下标。这样第一个下标始终是当前window里最大元素的下标。用一个clean函数来维护，clean是O(1)的。首先从左边去掉不在window里的下标，然后从右边开始去掉小于当前元素的下标。因为维护前是从大到小，所以维护后也是从大到小。然后用这个deque遍历nums就行了。


#### [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/description/), [Solution](SlidingWindow/Jump_Game_VI.py)
和239一样，用一个mono deque记录每个下标位置的最大score，每一步更新并保持window单调下降，且window里score最大的在第一个。

---

<div id='DFS'></div>

## DFS

#### [139. Word Break](https://leetcode.com/problems/word-break/), [Solution](DFS/Word_Break.py)
用backtrack往下一个个查，注意要缓存不然会超时。用`@lru_cache`缓存。

#### [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/), [Solution](DFS/Course_Schedule.py)
直接检测是否有环。中途传回True / False，方便检测到环的话快速结束。

#### [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/), [Solution](DFS/Course_Schedule_II.py)
一个拓扑排序。对每个点，如果已经标记了则跳过，如果已经临时标记了说明有环return。都没有则给一个临时标记，然后对所有相邻的点dfs。都dfs完了返回之后再去掉当前临时标记，做永久标记，然后放到拓扑序最前面。

#### [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/), [Solution](DFS/Longest_Increasing_Path_in_a_Matrix.py)
dfs返回从当前坐标开始的最长路径长度，用一个path_length来记录已计算过的格子

#### [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/description/), [Solution](DFS/Concatenated_Words.py)
直接dfs，对每个单词从每个下标分成两半，查找前一半和后一半是否在words里或者能表示成words里词的拼接。把words转换成set，加上memorization来提速。

#### [526. Beautiful Arrangement (similar to 46)](https://leetcode.com/problems/beautiful-arrangement/), [Solution](DFS/Beautiful_Arrangement.py)
T(N!), O(N)
直接backtrack，用一个self.count来记录当前有效permutation。每次idx到末尾就更新count。

#### [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/), [Solution](DFS/Number_of_Provinces.py)
直接dfs。检测连通分量个数。

#### [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/), [Solution](/DFS/Partition_to_K_Equal_Sum_Subsets.py)
T($k*2^N$), O(N)

先检测整体和是否能被k整除，可以的话用backtrack。每次往当前和里加一个元素，如果超过target_sum就直接返回，如果等于就count += 1然后当前和清零继续下一次backtrack，如果小于就依次往当前和里加入下一个元素并backtrack。注意就算从当前元素，不从头开始backtrack，且预先排序，依然在python上超时。

#### [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/description/), [Solution](DFS/Longest_String_Chain.py)
从长到短倒着dfs。这样可以不用每个字母每个位置都插入再尝试。

---

<div id='BFS'></div>

## BFS

#### [127. Word Ladder](https://leetcode.com/problems/word-ladder/description/), [Solution](BFS/Word_Ladder.py)
因为只要找到endWord就行，所以可以直接bfs+visited，不管中间是否有路径重叠。注意用一个interWord保存中间态，预处理wordList找到所有中间态，然后每一步转换成中间态之后再查找这个中间态可以到达哪些词。


---

<div id='DP'></div>

## DP

#### [72. Edit Distance](https://leetcode.com/problems/edit-distance/), [Solution](DP/Edit_Distance.py)

明明是DP不是DFS啊。如果作change，看看当前位置的character是否一样。如果作delete，在dp[i-1][j]上加1。如果作insert，在dp[i][j-1]上加1。取三个里面最小的。

#### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/description/), [Solution](DP/Interleaving_String.py)
用的算是brute force+cache，但其实可以用DP。dp[i][j]储存能否用s1[:i+1]和s2[:j+1]interleave出s3[:i+j+1]。

#### [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/), [Solution](DP/Longest_Increasing_Subsequence.py)
dp[i] = 以第i个元素结尾的最长递增子序列。di[i] = max(dp[j] + 1) if dp[i] > dp[j] for j < i.

#### [Contest 315 No.4 Count Subarrays With Fixed Bounds](https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/), [Solution](DP/Count_Subarrays_With_Fixed_Bounds.py)
先过一遍nums，记录每个坐标前最近的等于minK，等于maxK，超出范围的值的坐标，记为prev[0], prev[1], prev[2]。然后dp。dp[i] = dp[i-1]，如果nums[i]没超出范围，那么dp[i]再加上prev[0], prev[1]里更小的那个到prev[2]的距离。如果是负的就不加。

#### [322. Coin Change](https://leetcode.com/problems/coin-change/description/), [Solution](DP/Coin_Change.py)
很标准的dp题，对用到的硬币数量和amount大小进行dp。

#### [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/),[Solution](DP/Combination_Sum_IV.py)
对target进行dp，以nums里的每个数num作结尾都是不同的组合，然后dp(target-num)。用cache加记忆。

#### [403. Frog Jump](https://leetcode.com/problems/frog-jump/description/), [Solution](DP/Frog_Jump.py)
不是最优解，差不多是brute force+cache。可以用DP。用一个字典储存key:value, key是每个位置，value是能到这个位置的jump的长度的集合。最后如果最后一个位置在字典里，就说明可以跳到这里，否则不可以。

#### [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/), [Solution](DP/Course_Schedule_III.py)
先按结束时间排序，然后依次处理。维护到当前位置的上的最多的课，每个课的时长，和总时长。新的课来了之后，如果在当前时间直接上不超过lastDay，就直接放进heap里；如果超过了，duration大于之前的所有课的最大时长的话，不能放，否则无法维护是上的最多的课；如果小于之前的最大时长，则直接替换，可以维护是上的最多的课。因为是按结束时间排序，所以可以直接放进去替换。因为用了heap，所以总时长和之前上的课的时长也可以快速维护。

#### [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/description/), [Solution](DP/Cherry_Pickup.py)
第二次不用从n-1, n-1往回走了，直接从0, 0往右下出发两个路径，然后三维dp，dp[r1][c1][r2]，然后让两个点在同一反对角线上，这样c2 = r1 + c1 - r2。
#### [1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/description/), [Solution](DP/Valid_Palindrome_III.py)
直接dp，能不能变成palindrome取决于变成palindrome的最小次数是否小于k。dfs(i, j)如果s的i和j相等，则等于dfs(i+1, j-1)。否则说明i或者j之间要去掉一个，就等于1+min(dfs(i+1, j), dfs(i, j-1))。

#### [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/), [Solution](DP/Maximum_Profit_in_Job_Scheduling.py)
直接dp，用recursion+lru_cache可以直接过，用memorization的话就必须用二分搜索。dp(i) = dp(i+1)或者对第i个工作结束时间之后的所有工作j，profit[i]+dp(j)中最大的那个。

#### [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/), [Solution](DP/Minimum_Difficulty_of_a_Job_Schedule.py)
直接dp，dp(i, d)表示从第i个工作开始，还剩下d天。dp(i, d)等于在当天安排从i到j-1的工作，然后剩下的d-1天做j之后的工作，即dp(j, d-1)，对所有j > i里面最小的那一个。用lru_cache减少时间。

#### [1444. Number of Ways of Cutting a Pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/), [Solution](DP/Number_of_Ways_of_Cutting_a_Pizza.py)
3d的DP。能想到3d的话就还好。看起来dp还是专门留一行空的出来比较好，这样就不用初始化了。
#### [2222. Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/description/), [Solution](DP/Number_of_Ways_to_Select_Buildings.py)
dp[k][j]为在s[:i + 1]中选择长度为k的挑选方法数。同时分别保存其中以'0'和'1'结尾的方法数。dp[k + 1[j]考虑是否以s[j]结尾，不结尾直接用前一个，结尾再加上dp[k][j - 1]里面结尾元素和s[j]不同的方法数。
#### [2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/description/), [Solution](DP/Substring_With_Largest_Variance.py)
用dp，相当于max subarray的一个变体。分别判断所有两个字母的组合，最多25x26种组合，每个组合花O(n)的时间。判断当前字母并增减max_subarray后，根据后续是否无任何字母或两个字母都有还是其他，判断是中断本次循环还是重置窗口还是继续当前循环。

#### [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/), [Solution](DP/Maximum_Number_of_Non-overlapping_Palindrome_Substrings.py)
dp检查到i下标之前的子串，里面长度大于k的回文串的最大长度。注意这里对以i-1结尾的子串，只用检查长度为k和长度k-1的就行，更前面的不用检查。

---

<div id='OOD'></div>

## OOD

#### [1603. Design Parking System](https://leetcode.com/problems/design-parking-system/description/), [Solution](OOD/Design_Parking_System)
简单。