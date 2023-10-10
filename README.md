# LeetCode

My notes and solution for leetcode problems.

<div id="top"></div>
<button style="position: fixed; right: 10%; bottom: 10%"><a href=#top>Top</a></button>

## 目录

<ol>
  <li> <a href=#常用文档>常用文档</a></li>
  <li> <a href=#String>String</a></li> 
  <li> <a href=#List>List</a></li> 
  <li> <a href=#Hashmap>Hashmap</a></li> 
  <li> <a href=#LinkedList>Linked List</a></li> 
  <li> <a href=#Tree>Tree</a></li> 
  <li> <a href=#Trie>Trie</a></li> 
  <li> <a href=#Graph>Graph</a></li>   
  <li> <a href=#Heap>Heap</a></li> 
  <li> <a href=#Stack>Stack</a></li> 
  <li> <a href=#UnionFind>UnionFind</a></li> 
  ----
  <li> <a href=#Math>Math</a></li> 
  <li> <a href=#Prime>Prime</a></li> 
  <li> <a href=#Sort>Sort</a></li> 
  <li> <a href=#PrefixSum>PrefixSum</a></li> 
  <li> <a href=#BinarySearch>BinarySearch</a></li> 
  <li> <a href=#SlidingWindow>SlidingWindow</a></li> 
  <li> <a href=#TwoPointer>TwoPointer</a></li> 
  <li> <a href=#DFS>DFS</a></li> 
  <li> <a href=#BFS>BFS</a></li> 
  <li> <a href=#DP>DP</a></li> 
  <li> <a href=#Greedy>Greedy</a></li> 
  <li> <a href=#SQL>SQL</a></li>   
  <li> <a href=#OOD>OOD</a></li> 
</ol>

<div id='常用文档'></div>

## 常用文档

#### Python 包

[collections](https://docs.python.org/3/library/collections.html#counter-objects),
[heapq](https://docs.python.org/3/library/heapq.html), [itertools](https://docs.python.org/3/library/itertools.html), [bisect](https://docs.python.org/3/library/bisect.html)
[sortedcontainers](https://pypi.org/project/sortedcontainers/),

#### 数据结构

[segment tree](https://csacademy.com/lesson/segment_trees)

#### 算法-时间复杂度

O(n): Greedy, stack, bfs, dfs
O(n logn): sort, binary, tree like, heap
O(n^2): dp, Dijkstra

---

<div id='String'></div>

## String

#### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/), [Solution](String/Longest_Palindromic_Substring.py)

从每一个下标出发，以他为中心，检查奇数长度和偶数长度发的 substring 是否为 palindrome。还可以用 dp，dp[i][j]表示 s[i:j]是否是 palindrome。

#### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/description/), [Solution](String/Reverse_Integer.py)

先转成 str 然后 reverse 再拼起来。用到 rjust 来限制不会超出 64 位。用到 _ (1 - 2 _ (x < 0))来判断正负。

#### [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/), [Solution](String/Repeated_Substring_Pattern.py)

直接对每个长度可以被 s 长度整除的 substring 复制到和 s 一样长然后比较是否相等。

#### [2268. Minimum Number of Keypresses](https://leetcode.com/problems/minimum-number-of-keypresses/description/), [Solution](String/Minimum_Number_of_Keypresses.py)

直接过一遍 str，让频率高的放在第一个，9 个 button 放完了就放第二个，依次。每放一个字母就 count += number of ch in str \* 字母在 button 里的位置。

#### [2288. Apply Discount to Prices](https://leetcode.com/problems/apply-discount-to-prices/description/), [Solution](String/Apply_Discount_to_Prices.py)

简单，不过注意字符串里插入变量的格式：'str%格式'%(插入的东西)

#### [2609. Find the Longest Balanced Substring of a Binary String](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/), [Solution](String/Find_the_Longest_Balanced_Substring_of_a_Binary_String.py)

先过一遍找到每个连续 0,1 的开始下标和连续长度，然后对所有连续 0 找对应的下一个相邻连续 1，取 res = max(res, min(连续 0 长度，连续 1 长度) \* 2)。

#### [2663. Lexicographically Smallest Beautiful String](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/description/), [Solution](String/Lexicographically_Smallest_Beautiful_String.py)

不能有 palindrome，就是不能有任何偶数及奇数长度的 palindrome，就是不能有任意长为 2 或 3 的 palindrome，就是任意连续两个或三个字符不能相同。先把字符都转成 ascii 码，方便递增。因为是下一个最小的，所以从后往前递增。如果一个字符递增到了 k，说明要进位，就看前一个字符，当前字符先不管。如果不进位，且当前字符和前两个字符都不同，就把后面的依次放上 0， 1， 2 里面最小的且和前两个不同的字符。最后把数字转成字母。也算 greedy 吧。

#### [2734. Lexicographically Smallest String After Substring Operation](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description/), [Solution](String/Lexicographically_Smallest_String_After_Substring_Operation.py)

用数字记录字母，然后从第一个非 0 开始到他后面的第一个 0 为止，所有减 1，然后再转成字母。注意这个 window 的边界条件。

---

<div id='List'></div>

## List

#### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/), [Solution](List/Merge_Intervals.py)

先按区间起点排序，然后依次检查，如果当前的起点在前一个区间内就更新终点为两个区间里终点大的那个。

#### [163. Missing Ranges](https://leetcode.com/problems/missing-ranges/description/), [Solution](List/Missing_Ranges.py)

直接过一遍 nums，如果和前一个相差大于一则 ans.append 一个数或一个区间。注意 corner case，比如 nums = []，以及 lower 和 upper 处的情况。

#### [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/), [Solution](String/Excel_Sheet_Column_Title.py)

这里因为 A-Z 是用 1-26 编号的，所以每步都减 1，让余数范围变成从 0-25。商的部分不变或者只是把余 0 的部分变成 A。注意 ord()可以把字符转成 ascii 码，chr()把 ascii 码转成字符。

#### [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/description/), [Solution](List/Meeting_Rooms.py)

直接过一遍，检查每个 meeting 的开始时间是否早于前一个的结束时间。

#### [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/), [Solution](List/Minimum_Moves_to_Equal_Array_Elements.py)

其实很简单。要想到增加 n-1 个数等价于减少 1 个数。然后算每个数跟最小值的差就行了。

#### [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/description/), [Solution](List/Next_Greater_Element_III.py)

因为从左往右递减的序列没有比他更大的，所以对这个数从右往左找，找到第一个左边比右边小的数，左边是 i。从这个 digit 再往右走，找到最右边的比他大的 digit，j，交换这两个 digit。然后 reverse 从 i + 1 开始到最右边的 digits。

#### [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/), [Solution](List/Degree_of_an_Array.py)

先过一遍，用字典记录每个数字的频率，第一次和最后一次出现的位置。再过一遍字典，更新 max_fre 和 min_len。

#### [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/), [Solution](List/Partition_Array_into_Disjoint_Intervals.py)

还有个时间 O(N), 空间 O(1)的方法。记录 currMax, possibleMax, length。如果当前的小于 currMax，就说明当前元素必须在左边，所以更新 currMax， possibleMax 和 length。

#### [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/), [Solution](List/Kids_With_the_Greatest_Number_of_Candies.py)

简单，easy 题。

#### [1864. Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/description/), [Solution](List/Minimum_Number_of_Swaps_to_Make_the_Binary_String_Alternating.py)

因为只有两个字母，所以只要算其中一个字母不在正确位置上的最小位置数就行了。取两个字母里面这个数更小的那一个。

#### [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/description/), [Solution](List/Angle_Between_Hands_of_a_Clock.py)

直接算出时针和秒针的角度，然后取差的绝对值，再取跟补角里更小的那个。

#### [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/), [Solution](List/Merge_Strings_Alternately.py)

交替 append list。

#### [2012. Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array/description/), [Solution](List/Sum_of_Beauty_in_the_Array.py)

先从后往前过一遍记录到每个下标为止的最小值，然后从前往后，每步记录到前一个为止的最大值，比较当前与相邻的大小以及和前面所有的最大值、后面所有的最小值的大小。

#### [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/), [Solution](List/Maximum_Difference_Between_Increasing_Elements.py)

easy，一个指针过一遍，比较当前元素和之前最小元素，更新当前最小元素。

#### [2214. Minimum Health to Beat Game](https://leetcode.com/problems/minimum-health-to-beat-game/description/), [Solution](List/Minimum_Health_to_Beat_Game.py)

直接求和然后减去 armor 和 max(damage)里的最小值表示抵消一次攻击。完全是 easy 啊为什么会是 medium。

#### [2221. Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/description/), [Solution](List/Find_Triangular_Sum_of_an_Array.py)

用 Pascal Triangle 即组合数来算每个数在最终答案里用到的次数，然后直接一个个加上去。注意算组合数的时候要用//不要用/，不然后面会小数位有问题。也可以直接 recursive 做，不过很慢。

#### [2294. Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/), [Solution](List/Partition%20Array%20Such_That_Maximum_Difference_Is_K.py)

直接排个序然后从小到大分就行。

#### [2357. Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/), [Solution](List/Make_Array_Zero_by_Subtracting_Equal_Amounts.py)

先排序，然后依次处理值不一样的元素，被减去的值等于 max(nums)的时候就结束。

#### [2405. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/description/), [Solution](List/Optimal_Partition_of_String.py)

直接过一遍，用 set 记录，看到已经存在的就 res += 1 并重置 set。

#### [2546. Apply Bitwise Operations to Make Strings Equal](https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/), [Solution](List/Apply_Bitwise_Operations_to_Make_Strings_Equal.py)

要发现不同组合的规则。(0, 0) -> (0, 0)，(1, 0) -> (1, 1)，(0, 1) -> (1, 1)，(1, 1) -> (1, 0)。所以只有 0 的情况无法改变，只要有 1 个 1，就可以修改成任何情况。所以只要检查 s 和 target 是否同时全为 0 或者同时都含有 1 就行了。

#### [2643. Row With Maximum Ones](https://leetcode.com/problems/row-with-maximum-ones/description/), [Solution](List/Row_With_Maximum_Ones.py)

简单，每行过一遍就行了。

#### [2644. Find the Maximum Divisibility Score](https://leetcode.com/problems/find-the-maximum-divisibility-score/description/), [Solution](List/Find_the_Maximum_Divisibility_Score.py)

和前一题基本一样。

#### [2660. Determine the Winner of a Bowling Game](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/), [Solution](List/Determine_the_Winner_of_a_Bowling_Game.py)

简单，brute force 就行了。

#### [2672. Number of Adjacent Elements With the Same Color](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description/), [Solution](List/Number_of_Adjacent_Elements_With_the_Same_Color.py)

每改一个数只会影响当前位置和前一个位置的 adjacent element。所以就依次过一遍 query，每个 query 只看两个位置的变化就行了。

#### [2682. Find the Losers of the Circular Game](https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/), [Solution](List/Find_the_Losers_of_the_Circular_Game.py)

简单题，直接取余数就行。

#### [2683. Neighboring Bitwise XOR](https://leetcode.com/problems/neighboring-bitwise-xor/description/), [Solution](List/Neighboring_Bitwise_XOR.py)

标得 medium 不过实际 easy。依次根据 derived 判断当前位置是否取反就行了。

#### [2697. Lexicographically Smallest Palindrome](https://leetcode.com/problems/lexicographically-smallest-palindrome/description/), [Solution](List/Lexicographically_Smallest_Palindrome.py)

从中间往两边出发，每次保存对称位置上更小的那个元素，最后再把保存了的都拼起来。

#### [2698. Find the Punishment Number of an Integer](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/), [Solution](List/Find_the_Punishment_Number_of_an_Integer.py)

直接暴力解，每个数都算一遍所有组合看满不满足 punishment 条件。

#### [2712. Minimum Cost to Make All Characters Equal](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description/), [Solution](List/Minimum_Cost_to_Make_All_Characters_Equal.py)

分别让左半边和右半边一样，然后根据奇偶还有中间元素和中间元素两边是否相同判断最后的和。

#### [2716. Minimize String Length](https://leetcode.com/problems/minimize-string-length/description/), [Solution](List/Minimize_String_Length.py)

简单。

#### [2717. Semi-Ordered Permutation](https://leetcode.com/problems/semi-ordered-permutation/description/), [Solution](List/Semi-Ordered_Permutation.py)

简单。

#### [2735. Collecting Chocolates](https://leetcode.com/problems/collecting-chocolates/description/), [Solution](List/Collecting_Chocolates.py)

转 n 圈，每次更新每个位置上的最低 cost 加上转到这一圈需要的转圈 cost，每一圈都保存当前最低总 cost，最后输出。

#### [2733. Neither Minimum nor Maximum](https://leetcode.com/problems/neither-minimum-nor-maximum/description/), [Solution](List/Neither_Minimum_nor_Maximum.py)

简单，找不是最小最大值的。

#### [2749. Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/), [Solution](List/Minimum_Operations_to_Make_the_Integer_Zero.py)

根据操作次数 k 减去 k _ num2，剩下的就是由 2**i 组成的部分。bit_count()可以看 int 的二进制表示里面有几个 2**i。k 最小要大于等于这个 bit_count()，因为这样才能组合出来；最大要小于等于 num1 - k _ num2，因为每次操作最少会减去 1，所以最大不能超过剩下的数。从小到大遍历 k，检测到一个符合条件的 k 就输出，没有的话就 return -1。

#### [Snowflake Array Reduction](https://leetcode.com/discuss/interview-question/2550995/snowflake-OA), [Solution](List/Array_Reduction)

首先得到整个 array 的 mex。然后找到第一个使得当前 currMex 等于 mex 的位置，同时在 count 里减去已经用过的元素。然后在更新过的 count 里找到 nextMex，然后重复上一步。

---

<div id='Hashmap'></div>

## Hashmap

#### [1. Two Sum](https://leetcode.com/problems/two-sum/description/), [Solution](Hashmap/Two_Sum.py)

用 hashmap 储存与当前值的和为 target 的值，以及当前值的 index。继续查找每一个值，如果在 hashmap 里就输出储存的 index 和当前的 index。

#### [15. 3Sum](https://leetcode.com/problems/3sum/description/), [Solution](Hashmap/3Sum.py)

跟 2sum 基本一样，先排序，然后对每一个值把他当成 2sum 里的 k，然后对之后的做 2sum，依次重复 n 次。

#### [18. 4Sum](https://leetcode.com/problems/4sum/description/), [Solution](Hashmap/4Sum.py)

和 3sum 基本一样。另外这里面两个外部循环都有 if i == 0 or nums[i - 1] != nums[i]，是用来避免重复计算的。

#### [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/), [Solution](Hashmap/Two_Sum_III_-_Data_structure_design.py)

跟 Two Sum 一样，不过把 hashmap 的值的 index 换成了 count，因为只要找到是否有就行了不要下标。然后用 count 可以避免重复访问同一个元素。

#### [460. LFU Cache](https://leetcode.com/problems/lfu-cache/description/), [Solution](HashMap/LFU_Cache.py)

两个 map。一个保存 key, (frequency, value)对，一个保存 frequency, keys 对。key 是 OrderedDict。根据 key 查找 frequency，更新两个 map。同时维护当前有 key 的最小频率。

#### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/), [Solution](Hashmap/Subarray_Sum_Equals_K.py)

用一个 hashmap 记录到每个下标为止的子串合对应的子串数。对每个新下标，count 加上合为 当前子串合 - k 的子串数。

#### [1282. Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/), [Solution](HashMap/Group_the_People_Given_the_Group_Size_They_Belong_To.py)

先过一遍 group，找出每个 size 都有哪些人，然后对每个 size 里的那些人按 size 大小分组。

#### [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/), [Solution](HashMap/Minimum_Deletions_to_Make_Character_Frequencies_Unique.py)

用到了 Counter 和 SortedSet。先过一遍 Counter 统计每个字母出现了多少次，然后过一遍 Counter 统计每个出现频率的字母有多少个。然后把出现频率放到 sortedSet 里，从大到小，把每个出现频率的字母减少字母个数减一个，然后如果出现频率大于一（说明可以减少该字母）且该出现频率对应的字母数也大于一（说明确实有字母被减少了），那就在该频率减一的频率上加上该频率对应的字母数减一（因为有一个字母没有被减少）。

#### [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/), [Solution](Hashmap/Max_Number_of_K-Sum_Pairs.py)

跟 2sum 基本一样。不过用 count 来记录，然后每碰到一个匹配的就 count--，res++

#### [2488. Count Subarrays With Median K](https://leetcode.com/problems/count-subarrays-with-median-k/description/), [Solution](Hashmap/Count_Subarrays_With_Median_K.py)

得到 k 的下标，计算到 k 右边每个下标为止大于小于 k 的数的个数并保存在 hashmap 里；然后从 k 往左边一样计算，根据 hashmap 里的个数，加起来等于 0 或 1 的个数，就是从这个下标开始满足条件的 subarray 个数。

#### [2588. Count the Number of Beautiful Subarrays](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description/), [Solution](Hashmap/Count_the_Number_of_Beautiful_Subarrays.py)

要想到 beautiful subarray 就是 subarray 的依次 xor 等于 0 的意思。然后就是跟 560 一样了，用字典储存到每个位置的 xor 总和，然后每个新位置查一下字典里等于当前 xor 的个数，加到 count 上就行。这样从之前到当前位置的 xor 就为 0 了。

#### [2598. Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/), [Solution](Hashmap/Smallest_Missing_Non-negative_Integer_After_Operations.py)

按余数分类，同时记录当前余数个数。然后 q 从 0 开始，再 r 从 0 到 value - 1，遍历余数集，直到余数集里找不到下一个，就是不存在的，然后返回 q \* value + r

#### [2661. First Completely Painted Row or Column](https://leetcode.com/problems/first-completely-painted-row-or-column/description/), [Solution](HashMap/First_Completely_Painted_Row_or_Column.py)

先过一遍，统计每个元素的行列。然后根据 array，在每个位置对应的行列 count+1。然后如果有达到填满某一行或者某一列的就返回这个位置的 index。

#### [2671. Frequency Tracker](https://leetcode.com/problems/frequency-tracker/description/), [Solution](Hashmap/Frequency_Tracker.py)

两个 hashmap，分别记录每个数的频率和每个频率对应的数。每次增减都更新这两个 hashmap。

#### [2829. Determine the Minimum Sum of a k-avoiding Array](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/), [Solution](HashMap/Determine_the_Minimum_Sum_of_a_k-avoiding_Array.py)

简单，基本就是 2sum。

---

<div id='LinkedList'></div>

## Linked List

#### [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/), [Solution](LinkedList/Add_Two_Numbers.py)

创建一个新链表，如果 l1 或 l2 后面还有就继续延长这个链表

#### [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/), [Solution](LinkedList/Merge_k_Sorted_Lists.py)

merge sort 的方法做，分成两部分然后 merge 两部分分别的结果。

#### [86. Partition List](https://leetcode.com/problems/partition-list/description/), [Solution](LinkedList/Partition_List.py)

把比 x 小的和大于等于 x 的元素分别放到两个 list 里然后再现重新生成一个 linkedlist。

#### [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/), [Solution](LinkedList/Copy_List_with_Random_Pointer.py)

我用的简单的先复制再建立联系，可以用 recursive 的方法直接在复制的时候就建立联系。

#### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/), [Solution](LinkedList/Linked_List_Cycle.py)

遍历链表，把见过的放进 set，之后如果碰到之前放进 set 过的就是 cycle，否则不是。

#### [146. LRU Cache](https://leetcode.com/problems/lru-cache/description/), [Solution](LinkedList/LRU_Cache.py)

用双链表做。保存 head 和 tail，然后自己写一个 addNode 和 deleteNode 函数。另外用一个 dict 保存 key 和对应 node 的指针。get 的时候删掉对应 node 并再次加到头部；put 的时候如果已经在里面就删掉，然后如果 dict 还是满的就说明 put 的是新元素，删掉 tail 前的 node，然后再把新 node 的加到头部。

#### [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/description/), [Solution](LinkedList/Add_Two_Numbers_II.py)

过两遍 linkedlist 乘 10 相加，然后加起来再除 10 取余从尾到头建个新 linkedlist。

#### [725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/description/), [Solution](LinkedList/Split_Linked_List_in_Parts.py)

根据剩余总数和剩余组数，如果能整除下一组就有正好整除那么多个 node，不能的话就是整除向上取整那么多个。

#### [2046. Sort Linked List Already Sorted Using Absolute Values](https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/description/), [Solution](LinkedList/Sort_Linked_List_Already_Sorted_Using_Absolute_Values.py)

先过一遍按正负分到两个 list 里，然后再按顺序连起来。

---

<div id='Tree'></div>

## Tree

#### [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/description/), [Solution](Tree/Unique_Binary_Search_Trees_II.py)

写一个 helper 生成两个数之间的所有二叉树，然后以每个数为 root，递归他的左右子树，然后组合起来以这个数为 root 的树。

#### [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/), [Solution](Tree/Binary_Tree_Maximum_Path_Sum.py)

写一个 helper 算从每个 node 开始的子树下的 max path sum 和以这个 node 为终点的最大 path sum。然后返回 helper[0]就行了。

#### [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Search_Tree.py)

跟下面一个基本一样，不过利用了 BST 的结构，直接判断当前节点的值，如果在 p，q 之间就是找到了，小于更小的或者大于更大的就去另一边找。

#### [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Tree.py)

用一个 helper 判断在当前子树中是否检测到 p 或 q。在 root，helper(root.left)，helper(root.right)中如果有两个检测到了就是找到了 LCA，修改全局变量 self.ans。每一层返回 curr or 上面两个，这样就算找到了 LCA，后续返回的也是 True 就是 1，之后不会重复修改全局变量。

#### [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/description/), [Solution](Tree/Boundary_of_Binary_Tree.py)

直接分别取 left boundary, leaves, and right boundary。

#### [666. Path Sum IV](https://leetcode.com/problems/path-sum-iv/description/), [Solution](Tree/Path_Sum_IV.py)

用每个 num 前两位表示一个 node，然后建 dict 储存值。dfs 根据 node 数值关系遍历，到每个 node 就在当前和上加上当前 node 的 value。然后到 leave 的时候就在 self.ans 上加上当前和。

#### [894. All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/description/), [Solution](Tree/All_Possible_Full_Binary_Trees.py)

recursion 做，对 n 个 node 的树递归左右子树从 0 到 n - 1。同时用一个字典记录 n 个 node 的树的所有组合方式，之后递归到的时候就不用重复计算。

#### [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/), [Solution](Tree/Lowest_Common_Ancestor_of_Deepest_Leaves.py)

bfs 找到 deepest leaves，并记录每个 node 的 parent。从最底层的 leaves 开始，回溯 parent，直到只剩某一层一个 parent。

#### [1676. Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Tree_IV.py)

和基本情况差不多，不过这次不是检测是否只有两个，而是检测是否所有 node 都被在当前子树下找到了。

#### [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/), [Solution](Tree/Step-By-Step_Directions_From_a_Binary_Tree_Node_to_Another.py)

做个辅助函数，在树里找到对应元素并记录路径。只有找到对应元素才会返回 True，否则都返回的是空 list，所以只有找到了才会记录 path。并且是倒着记录的。然后把 start 和 dest 相同的 prefix 去掉，这里就是从 LCA 开始的路径了，到 start 的都替换成 U，再加上到 dest 的路径就行了。

#### [2471. Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/), [Solution](Tree/Minimum_Number_of_Operations_to_Sort_a_Binary_Tree_by_Level.py)

用两个 queue 按层 bfs 遍历树，然后对每层求 min swap。重点是 min swap。注意 iterative traversal 的时候就用普通 stack 就行，然后先后顺序反过来。

#### [2673. Make Costs of Paths Equal in a Binary Tree](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description/), [Solution](Tree/Make_Costs_of_Paths_Equal_in_a_Binary_Tree.py)

在每个点让他的左右子路径相等。res 加上左右子路径的差，然后更新这个点的 cost 到本来的 cost 加上子路径的 cost。

---

<div id='Trie'></div>

## Trie

就是 nested hashmap。一开始就是一个{}，每一层就加一个 key，每到一个终点就在终点的 hashmap 里加一个'$'的 key 表示到达终点了。

#### [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/), [Solution](Trie/Design_Add_and_Search_Words_Data_Structure.py)

用 Trie 保存加进去的 word，然后每次 search 检查。

#### [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/), [Solution](Trie/Word_Search_II.py)

先用一个 trie 记录所有 word，然后从 board 的每个位置开始 dfs。如果在 trie 里找到了，就去掉这个词。如果某个叶节点到底了而且已经找到过了，就去掉这个叶节点。

#### [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/description/), [Solution](Trie/Design_In-Memory_File_System.py)

Trie 里有三个东西，isFile 看这个是 file 还是 directory，children 保存当前目录下所有 file 和 directory，content 就是 content。查找 path 的时候直接往下一路走就行了，因为 childer 是一个 defaultdict，如果不存在会自动新建一个。

#### [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/description/), [Solution](Trie/Search_Suggestions_System.py)

用 Trie 记录 product，并在每一层用 suggestion 记录三个词，然后对 word 每个字母到每一层的时候直接访问对应的 suggestion。还可以用 sort + binary search。

---

<div id='Graph'></div>

## Graph

#### [815. Bus Routes](https://leetcode.com/problems/bus-routes/description/), [Solution](Graph/Bus_Routes.py)

先预处理一遍，每个 bus route 当成一个 node，建立 node 之间的边，然后再 bfs。预处理的部分可以优化。

#### [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/), [Solution](Graph/Find_Critical_and_Pseudo-Critical_Edges_in_Minimum_Spanning_Tree.py)

先排序，然后用 Kruscal 找出一个最小生成树并记录这个树的最小权。然后对每个边考虑不带这个边和强制带这个边，再用 Kruscal 看是否能组成等于最小权的最小生成树，来判断这个边是否是 critical 或 seudo critical 的。把 union find 写成一个类，方便后面每次 Kruscal 里方便调用。

#### [1615. Maximal Network Rank](https://leetcode.com/problems/maximal-network-rank/description/), [Solution](Graph/Maximal_Network_Rank.py)

简单，统计一下每个 node 的度然后暴力就行了。注意相连的 node 的 network rank 要减一。

#### [2115. Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/), [Solution](Graph/Find_All_Possible_Recipes_from_Given_Supplies.py)

拓扑排序，排序路上经过的入度为 0 的点就是可以的 recipe。

---

<div id='Heap'></div>

## Heap

#### [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/), [Solution](Heap/Meeting_Rooms_II.py)

Use a heap to keep the end time of each room. Process meetings by their start time. If the start time is earlier than the earliest endtime, then it means more room is needed. Otherwise just allocate the already finished room to the current meeting.
只用保存每个 meeting room 的结束时间就行了，如果新的 meeting 在某个结束后才开始就直接替换那个结束时间，即把新的 meeting 安排在旧的 meeting 后面。

#### [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/), [Solution](Heap/Find_Median_from_Data_Stream.py)

建一个最大堆和一个最小堆，保存他们的大小，每次有新的数进来就让他进最小或最大堆，保持最大堆和最小堆个数相等或者多 1。

#### [767. Reorganize String](https://leetcode.com/problems/reorganize-string/description/), [Solution](Heap/Reorganize_String.py)

先算出每个字母的出现次数，然后依次把出现次数最多或第二多的 append 到末尾。用 heap 来看出现最多的字母。

#### [2158. Amount of New Area Painted Each Day](https://leetcode.com/problems/amount-of-new-area-painted-each-day/description/), [Solution](Heap/Amount_of_New_Area_Painted_Each_Day.py)

实际是用 sortedlist 做的。还可以用 segment tree 做。先记录所有 query 的 start 和 end 以及对应 query 的 index，还有类型用来区分这是 start 还是 end。比如(start, index, type)。sortedlist 是想象所有区间叠在一起，然后按 index 先后区分区间里数轴的距离。一根垂直于数轴的竖线扫过去，碰到 start 就把对应区间的 index 放入 sortedlist，遇到 end 就把对应区间的 index remove。然后每一步把 res 里对应 sortedlist 里最小的 index 那一个增加。如果是按数轴上一个个点移动的竖线就每次加一，因为是一步步移动的。如果是按记录下来的每个 query 来移动，就可以每次加上 pos 对应 start/end，减去 last_pos 就是前一个 query 的 pos。

#### [2386. Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/description/), [Solution](Heap/Find_the_K-Sum_of_an_Array.py)

先得到所有正数的和，这是可能得最大和。然后开始去掉和里的正数，或者加上剩下的负数，这两个都等价于从最大和里减去 nums 里的绝对值。因为是从最大和往下，所以把 nums 按绝对值排序之后依次减去每个值，并且每一步考虑加上 nextSum - absNum[idx + 1]和 nextSum + absNum[idx] - absNum[idx + 1]两种情况，即是否减去下标 idx 的值。每一步的结果都放到一个最大堆里，下一步再从最大堆里取，保证了是从 maxSum 依次往下递减。absNum 排序过，也是用来保证 maxSum 依次递减。

#### [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/description/), [Solution](Heap/Meeting_Rooms_III.py)

用两个 min heap，一个保存可以用的房间，一个保存使用中的房间，以结束时间为关健字。每一步先把结束时间小于当前开始时间的都挪到可用房间，如果当前有可用房间则直接用，没有的话则推迟当前 meeting 到下一个可以用的房间为止。

#### [2662. Minimum Cost of a Path With Special Roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/), [Solution](Heap/Minimum_Cost_of_a_Path_With_Special_Roads.py)

Dijrastra 的想法，因为所有 special road 的终点从任何起点都是可达的，所以里面每一步都要更新到所有重点的距离。每次取出最小距离，然后更新先到这个点，然后走到其他 road 的起点，然后再走 special road 到相应终点的距离。最后 res 返回先到每一个终点，再正常走到 target 的距离，这些的最小距离。

---

<div id='Stack'></div>

## Stack

#### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/), [Solution](Stack/Valid_Parentheses.py)

stack 记录正括号，对每个反括号用字典取正括号看是不是在 stack 末尾，且 stack 不空。最后检查 stack 是否空。

#### [71. Simplify Path](https://leetcode.com/problems/simplify-path/description/), [Solution](Stack/Simplify_Path.py)

按/分割，然后根据.和..决定 pop 还是不管还是加入 stack，最后用/连接。

#### [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/), [Solution](Stack/Largest_Rectangle_in_Histogram.py)

可以用 stack 是因为实际只有 n 个 rectangle 要检查。每个 height，和这个 height 往左往右到第一个比他矮的 height 为止，这个 rectangle。假设已经有一个 stack，里面放着从低到高排列的 height，检测到新的 height 比 stack 末尾的 height 低的时候就开始依次 pop。因为是从低到高，所以每 pop 一个就根据这个的 height 和他前一个的下标计算面积。到末尾再把剩下的全部 pop 出来。

#### [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/), [Solution](Stack/Maximal_Rectangle.py)

对每一行，保存到当前位置为止的连续 1 的个数。然后叠起来，从列来看，每一列就是一个 histgram，就转化成了上一题 84。所以预处理出 n 个 hist 之后，只用再对每一列做一次 largest rectangle 就可以了。

#### [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/description/), [Solution](Stack/Remove_Duplicate_Letters.py)

让 stack 里保存到当前位置为止的最小 substring。如果当前元素不在里面就放进来。每次新元素进来，把前面 stack 里比这个大的且后面还有的 pop 出去。

#### [394. Decode String](https://leetcode.com/problems/decode-string/description/), [Solution](Stack/Decode_String.py)

用两个 stack 分别保存括号外面的数字和字母。碰到\[就把当前的数字和字母加到 stack 里，然后碰到\]的时候就把当前字母乘上数字 stack 里最后一个的倍数，再在前面加上字母 stack 的最后一个。

#### [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/), [Solution](Stack/Next_Greater_Element_I.py)

首先预处理一个 monostack，找到每个数的 nextGreater。每步从末尾 pop 出 stack 里比当前元素小的元素的下标。用字典记录那个元素:当前元素。然后过 nums1，在字典里找相应的元素。

#### [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/description/), [Solution](Stack/Next_Greater_Element_II.py)

过一遍 monostack，每次 pop 出比当前小的元素的下标并更新那些元素的 nextGreater。更新完之后把当前下标放进 stack。再过第二遍，这样之前 nextGreater 在左边的也可以被更新了。

#### [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/description/), [Solution](Stack/Asteroid_Collision.py)

用 stack 记录 asteroid， 每个新的如果往右那么不会和 stack 里已有的碰撞，直接加进去；如果往左就一直碰撞到自己消失或者没有可以碰撞的为止。

#### [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/), [Solution](Stack/Daily_Temperatures.py)

简单，每次 pop 出比当前低的 temperature 的下标就行。

#### [768. Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/), [Solution](Stack/Max_Chunks_To_Make_Sorted_II.py)

和 769 完全没区别啊。

#### [769. Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/description/), [Solution](Stack/Max_Chunks_To_Make_Sorted.py)

保存一个递增 stack，里面每个数就是一个 chunk 的最大元素。每次把大于当前元素的都 pop 出来。当前元素前面比当前大的元素都必须和当前元素在同一个 chunk 里。

#### [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/description/), [Solution](Stack/Score_of_Parentheses.py)

也可以用 divide conquer 做。不过这里用 stack。记录当前 frame 的 score，如果是(就是 0，是)就把当前 frame\*2 再加到更前一个上面。

#### [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/), [Solution](Stack/Online_Stock_Span.py)

保存每个 price 和他前面小于等于他的 price 的个数。每次把 stack 末尾小于等于当前 price 的 pop 出来就行。

#### [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/), [Solution](Stack/Sum_of_Subarray_Minimums.py)

过两遍数组，找到每个元素右边第一个比他小的元素的下标，以及左边第一个小于等于他的元素的下标。在这两个之间，所有数组都以他为最小值。所以再过一遍数组，求这两个下标之间，包含这个元素的总数组数就行了。

#### [1996. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/), [Solution](Stack/The_Number_of_Weak_Characters_in_the_Game.py)

排序，atack 从小到大，defence 从大到小，然后从后往前遍历，保存目前见过的最大 defence。因为 atack 从小到大，所以往前走的时候 atack 一直变小。因为 defence 从大到小，所以不会出现倒挂的情况。
还可以用 greedy，就是先过一遍，找出对每个 atack，比他大的那些 atack 里面，可能的最大 defence。然后再过一遍，对每个 atack，查找比他大的 atack 里面的最大 defence 是否比他自己的 defence 大。

#### [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/description/), [Solution](Stack/Buildings_With_an_Ocean_View.py)

维护一个 decreasing stack。每次从 stack 末尾开始把高度小于等于当前高度的 idx 都 pop 掉。

#### [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/description/), [Solution](Stack/Sum_of_Subarray_Ranges.py)

和 907 基本一样，不过这次要对每个元素，同时找出以他为最大值的数组数和以他为最小值的数组数。每次这两个相减就行了。

#### [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/description/), [Solution](Stack/Removing_Stars_From_a_String.py)

直接一个 stack 往前走，碰到\*就 pop 就行了。

#### [2645. Minimum Additions to Make Valid String](https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/), [Solution](Stack/Minimum_Additions_to_Make_Valid_String.py)

写的是 dp，不过其实是 stack，因为只有一维。对每个字符，根据他前面的字符分类讨论就行了。

#### [2696. Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/), [Solution](Stack/Minimum_String_Length_After_Removing_Substrings.py)

用 stack，从头往后，监测到 AB 或者 CD 就 pop。

#### [2751. Robot Collisions](https://leetcode.com/problems/robot-collisions/description/), [Solution](Stack/Robot_Collisions.py)

先排序，然后按照 position 顺序从左到右，用 stack 记录已有的 robot，如果新加进来的是往左的就一直和 stack 末尾往右的 robot 碰撞，直到末尾不往右或者其中一个消失。一开始排序的时候记得把原来在 position 里的顺序也记录一下，最后按这个再排一次序，然后输出每个 robot 的 health。

---

<div id='UnionFind'></div>

## Union Find

可以用来检查集合连通性。

#### [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/), [Solution](UnionFind/Most_Stones_Removed_with_Same_Row_or_Column.py)

对每个石头，连接他的 row 和 col。因为 row 数有限，所以 col 直接+10001 就行。最后检查有多少连通集。

#### [959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/description/), [Solution](UnionFind/Regions_Cut_By_Slashes.py)

把每个格子分成四个三角形，根据每一个位置是\或/或者空格，连接格子里的三角形。然后连接相邻格子的三角形。最后统计有多少三角形的 root 是他自己，即连同集个数。

#### [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/description/), [Solution](UnionFind/Number_of_Closed_Islands.py)

用 unionfind 做的，但里面废操作太多了。可以用 bfs，每次开始 bfs 的时候设置一个 boolean isclosed = True，之后如果碰到边界就改成 False。这样依次 bfs 就可以了。

#### [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/), [Solution](UnionFind/Number_of_Operations_to_Make_Network_Connected.py)

找出不联通集的个数，返回个数减一。

#### [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/), [Solution](UnionFind/Remove_Max_Number_of_Edges_to_Keep_Graph_Fully_Traversable.py)

用 union find 来记录 alice 和 bob 的边是否都是连通的。最后检查加进去的边是不是等于 n - 1。这里 UF 用的是一个列表，因为正好 node 都是从 1 到 n 标记的。用 dict 也可以，就是中间复制的时候要手动写一个 deep copy。

#### [1627. Graph Connectivity With Threshold](https://leetcode.com/problems/graph-connectivity-with-threshold/description/), [Solution](UnionFind/Graph_Connectivity_With_Threshold.py)

先预处理，对 threshold 到 n 的每个数字用 union find 建立连通分量，然后每个 query 判断是否在一个等价类里面。

#### [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/), [Solution](UnionFind/Checking_Existence_of_Edge_Length_Limited_Paths.py)

先对 queries 和 edges 分别排序，然后对每个 query，把 distance 小于当前 query 的 limit 的那些 edge 用 union 连起来，然后用 find 判断当前 query 的 p 和 q 是否连同。因为只连接了小于当前 limit 的所有边，所以直接判断就行，不用另外看每个边的 distance。

#### [2493. Divide Nodes Into the Maximum Number of Groups](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/), [Solution](UnionFind/Divide_Nodes_Into_the_Maximum_Number_of_Groups.py)

对每一个 node 做 bfs 就可以得到最大 group 数。用 union find 来记录连通分量。其实不用 union find 也可以，只要记录了连通分量就可以。

#### [2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/description/), [Solution](UnionFind/Count_the_Number_of_Complete_Components.py)

先找到连通集，然后看每个连通集是否是 complete 的。

---

<div id='Math'></div>

## Math

#### [50. Pow(x, n)](<https://leetcode.com/problems/pow(x,-n)/description/>), [Solution](<Math/Pow(x,_n).py>)

暴力会超时，所以根据 n 的二进制表示来考虑结果里有哪些 x 的二次 power。可以用 bitmask 或者 recursion。从小到大可能会超出 float 范围，所以可以限制将超出范围的时候返回 0（因为答案不会超出范围，中间的 power 超出范围就说明是负幂就是除）。也可以从大到小做，不会超出范围。

#### [400. Nth Digit](https://leetcode.com/problems/nth-digit/description/), [Solution](Math/Nth_Digit.py)

先找到这个数有多少位，然后找出具体是哪个数，然后取余找到具体是这个数的哪一位。

#### [1359. Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/), [Solution](Math/Count_All_Valid_Pickup_and_Delivery_Options.py)

就是插空，每多一对就在之前的所有里面的空隙之间插入。

#### [2850. Minimum Moves to Spread Stones Over Grid](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/), [Solution](Math/Minimum_Moves_to_Spread_Stones_Over_Grid.py)

首先看哪些位置大于 1，哪些位置等于 0，然后放进 list。大于 1 的放进去 x - 1 次，x 是具体数值，表示这个位置要被分配 x - 1 次。然后计算这两个 list 里面每两个点之间的曼哈顿距离，这里用了 scipy.spatial.distance.cdist 这个函数。然后就是一个找矩阵最小分配 cost 问题，用的算法是[Hungatian](https://en.wikipedia.org/wiki/Hungarian_algorithm)算法。直接用了 scipy.optimize.linear_sum_assignment 这个函数。

---

<div id='Prime'></div>

## Prime

- 筛法
- all primes are either 2， 3， 或者 6n - 1/6n + 1 for some n
  范围不大可以用筛法，这样筛一次就行了。但是空间需求很大。如果数字范围很大就用 prune，只有用到了才会算空间。

#### [2523. Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range/description/), [Solution](Prime/Closest_Prime_Numbers_in_Range.py)

主要注意怎么筛素数。对小于 x 的素数，从 2 到 sqrt(x)为止，如果 i 是素数就把 i 的所有倍数都标位合数，依次标记。最后把没被标记为合数的拿出来，就剩下的是素数。

#### [2572. Count the Number of Square-Free Subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/description/), [Solution](Prime/Count_the_Number_of_Square-Free_Subsets.py)

其实算是 dp 了。注意空集的时候返回的是 1，因为要和其他情况组合，其他子集里可能有元素，所以不返回 0。最后再只减去一个 1，就是所有子集都为空集的情况。

#### [2614. Prime In Diagonal](https://leetcode.com/problems/prime-in-diagonal/description/), [Solution](Prime/Prime_In_Diagonal.py)

用 prune，然后对每个对角线上的元素，用 sqrt 之后再 prune 了的子集来判断是否是素数。用到了 lambda 函数，filter，all，集合的并｜，sorted。

---

<div id='Sort'></div>

## Sort

#### [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2/problem), [Solution](Sort/Minimum_Swaps_2.py)

把数组看成一个图，每个数字是一个节点，从当前位置到排序好后应该在的位置有一条边，得到一些不交的圈。最后 swap 数 = sum(每个圈的大小 - 1)。按顺序遍历排序后的数组，用元组保存原始位置，通过访问原始位置来遍历整个圈。用一个 list 或者 set 来 track 是否每个元素都 visit 了。

#### [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/), [Solution](Sort/Kth_Largest_Element_in_an_Array.py)

最简单的是用 heap。然后可以用快速选择，每一步选一个 pivot 然后 partition，返回 partition 后的 pivot 下标。如果下标等于 k smallest 就返回，否则根据相对大小在 pivot 左边或者右边继续找。可以 iterative 来做，就是给一个 start 一个 end，每一步把 start 或 end 重新定位到 partition 之后的 pivot，直到 start 等于 end。

#### [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/), [Solution](Sort/Find_K-th_Smallest_Pair_Distance.py)

比较复杂，对 pair distance 用 binary search，用一个 possible 表示是否有 k 或更多个 pair 的 distance 小于等于 v。用 prefix sum 来简化对 possible 的计算。直接抄的，之后重写一遍。

#### [937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/), [Solution](Sort/Reorder_Data_in_Log_Files.py)

自定义 key 排序，先找一遍把数字都找出来，剩下的分别按 content 和 identifier 排序。也可以统一一起排序，key 为另一个还是，用来生成一个 tuple 产生顺序。注意 str.split()可以定义 maxsplit。

#### [1152. Analyze User Website Visit Pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/description/), [Solution](Sort/Analyze_User_Website_Visit_Pattern.py)

用一个 dict 记录每个人的访问顺序，然后用 Counter 记录每个人访问过的网站的所有 combination，然后用 max，key=lambda x:pattern[x]取出 pattern 里面最大且字典序最小的元素那个

#### [1356. Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/), [Solution](Sort/Sort_Integers_by_The_Number_of_1_Bits.py)

直接做。可以一行解决其实。注意 python 有 bin 函数，直接返回一个数的二进制表达。另外 count 函数直接返回一个数里某个数的个数。

#### [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/), [Solution](List/Maximum_Units_on_a_Truck.py)

简单的单位容量背包问题，直接按价值从大到小放就行了。

#### [2055. Plates Between Candles](https://leetcode.com/problems/plates-between-candles/description/), [Solution](Sort/Plates_Between_Candles.py)

记录下所有 candle 的位置，然后对每个 query 用二分，找到从左往右和从右往左的第一个 candle，然后两个之间的距离减去两个之间的 candle 数，就是 plate 数。

#### [2340. Minimum Adjacent Swaps to Make a Valid Array](https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/), [Solution](Sort/Minimum_Adjacent_Swaps_to_Make_a_Valid_Array.py)

直接找到第一个最小元素和最后一个最大元素，然后算把他们放到正确位置的 swap 数。

#### [2659. Make Array Empty](https://leetcode.com/problems/make-array-empty/description/), [Solution](Sort/Make_Array_Empty.py)

考虑分别 pop 掉每一组递增序列。记录原始位置然后排序。从小到大，如果原始位置比前一个小就说明当前元素在原数组里属于一组新的数。res 加上剩下的所有元素，因为要把剩下的都 rotate 一遍才能 pop 掉当前组的所有元素。而且也当前组的最后一个元素也肯定是在末尾，所以要完全 rotate 一遍。因为如果末尾元素大于当前组最大元素，那就属于当前组。如果小于那就已经在前面的迭代里被 pop 掉了。

---

<div id='PrefixSum'></div>

## Prefix Sum

#### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/), [Solution](PrefixSum/Product_of_Array_Except_Self.py)

实际是 prefix suffix product。先从头往后，记录 prefix product。然后从后往前，在之前对应的 prefix product 上再乘上 suffix product。

#### [370. Range Addition](https://leetcode.com/problems/range-addition/description/), [Solution](PrefixSum/Range_Addition.py)

先用 cache 记录每个 query 开始的位置和结束的下一个位置，然后过一遍，期间每个位置的 currSum 加上对应的 cache。

#### [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/description/), [Solution](PrefixSum/Corporate_Flight_Bookings.py)

同 370。一模一样只能说。

#### [1094. Car Pooling](https://leetcode.com/problems/car-pooling/description/), [Solution](PrefixSum/Car_Pooling.py)

同 370，不过这次用的是 dict 来当 cache。上面一个其实也可以，不过因为上面本来就要返回一个 list 所以直接用了 list。

#### [2234. Maximum Total Beauty of the Gardens](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/description/), [Solution](PrefixSum/Maximum_Total_Beauty_of_the_Gardens.py)

先排序，然后从没到 target 的开始从后往前，看把后 j 个补到 target 需要多少。然后用 new 减去这个，就是剩下来可以用在前面补 partial 的。先算一个 prefix sum 计算把前 i 个补到和第 i 个一样多需要多少 cost。然后用剩下来的再 cost 里二分查找，找到最多可以补到多少。然后算 partial 和 full 分别的分数。

#### [2281. Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/description/), [Solution](PrefixSum/Sum_of_Total_Strength_of_Wizards.py)

先算出每个元素右边第一个比他小的下标，左边第一个小于等于他的下标，然后对每个元素，计算所有以他为最小元素的数组的和。这里要用两次 prefix sum，并且最后算的时候数组和是这样 racc _ ln - lacc _ rn 的形式。自己想大概是想不出来的，只能看碰到的话记不记得了。

#### [2536. Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/description/), [Solution](PrefixSum/Increment_Submatrices_by_One.py)

对每一行做一次 prefix sum。另外也可以用 2dcache 来做，在每个矩形的左上角、右下角外+1，右上角外、左下角外-1 不过还没看懂，之后有兴趣可以看看[这里](https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-with-visualization-clean-concise/)。

#### [2615. Sum of Distances](https://leetcode.com/problems/sum-of-distances/description/), [Solution](PrefixSum/Sum_of_Distances.py)

用 dict 存数和对应的下标。距离里面把每个绝对值号拆开，然后就可以有公式了。对每个数，先算一个 prefix sum，然后每个下标里面套公式和 prefix sum 就行了。

#### [2670. Find the Distinct Difference Array](https://leetcode.com/problems/find-the-distinct-difference-array/description/), [Solution](PrefixSum/Find_the_Distinct_Difference_Array.py)

先过一遍，保存 prefix 和 sufix sum，然后直接算结果。

---

<div id='BinarySearch'></div>

## Binary Search

#### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/), [Solution](BinarySearch/Search_in_Rotated_Sorted_Array.py)

先通过 left 和 mid 的大小关系判断转折点在左边还是右边，然后再通过 target 和递增那一边的两端的大小关系判断 target 在哪边。

#### [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/), [Solution](BinarySearch/Search_a_2D_Matrix.py)

bisect_left 返回下标 i，这之前的所有元素严格小于搜索的元素 x，i 及 i 之后的元素大于等于 x。先搜索所有行的第一个元素。如果返回的下标元素等于 target 则结束。否则说明 target 在下标对应的那一行（可能超出）。然后在下标对应的行再次搜索，判断搜索出来的元素是否等于 target。

#### [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/), [Solution](BinarySearch/Search_in_Rotated_Sorted_Array_II.py)

和 33 基本一样，加一个步骤每轮如果 left 和 right 和相邻的相等就往中间移动，这样保证 nums[left] <= nums[mid]的时候转折点肯定在右边，否则在左边的话说明 mid 到 right 为止全都相等，那 right 就会一直往左走直到不相等。

#### [704. Binary Search](https://leetcode.com/problems/binary-search/description/), [Solution](BinarySearch/Binary_Search.py)

简单。可以把相等情况放在第一个判断，这样可以不用每次都运行到最底端，而且可以避免中间 out of range。

#### [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/), [Solution](BinarySearch/Peak_Index_in_a_Mountain_Array.py)

每次判断 mid 和他左右元素的大小，如果不是 mid - 1 < mid > mid + 1 就说明不是 peak，根据落在 peak 左边或右边决定下一步 binary 的方向。

#### [1870. Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/), [Solution](BinarySearch/Minimum_Speed_to_Arrive_on_Time.py)

从最小速度到最大速度之间二分搜索。另外用一个函数来验证每个速度是否能达到。

#### [2300. Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/), [Solution](BinarySearch/Successful_Pairs_of_Spells_and_Potions.py)

对 potions 排序，然后在里面找对应每个 success/spell 的下标，有了下标就可以直接得到个数了。

#### [2439. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array/description/), [Solution](BinarySearch/Minimize_Maximum_of_Array.py)

就是 snowflake 的 oa。不过有 O(n)解法，greedy，明天再看看。

#### [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/), [Solution](BinarySearch/Minimum_Cost_to_Make_Array_Equal.py)

cost 函数是凸函数，所以可以用二分法来找这个最小值。每一步计算 mid 和 mid + 1 的 cost，判断最小值点在 mid 的左边还是右边，然后二分就行了

#### [2517. Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/), [Solution](BinarySearch/Maximum_Tastiness_of_Candy_Basket.py)

感觉 binary sort 这种的越来越多了。对 tastiness 二分，每步检查是否有一组 k 个 candy，tastiness 大于等于 mid。

#### [2552. Count Increasing Quadruplets](https://leetcode.com/problems/count-increasing-quadruplets/description/), [Solution](BinarySearch/Count_Increasing_Quadruplets.py)

把(i, j)和(k, l)分开看。保存一个 sortedlist，每加进来一个新的 j 就放到里面。对每一个 j，再对 k 循环。记录比 nums[j]大的 nums[k]的个数，也就是每个 k 右边比 nums[j]大的 nums[l]的个数。然后在 sortedlist 里二分找比 nums[k]小的 nums[i]的个数。两个相乘再加到总的 res 上。

#### [2610. Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/), [Solution](Hashmap/Convert_an_Array_Into_a_2D_Array_With_Conditions.py)

counter 看一下每个数出现次数，然后依次往里面放就行了。

#### [2616. Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/), [Solution](BinarySearch/Minimize_the_Maximum_Difference_of_Pairs.py)

mini max 问题用二分法。这里每次检测 mid 这个最大 difference 可不可以达到。因为排序后的所有最小 difference 肯定出现在相邻元素之间，所以每次检测的时候只用检测那些相邻的元素就行了。

#### [2718. Sum of Matrix After Queries](https://leetcode.com/problems/sum-of-matrix-after-queries/description/), [Solution](BinarySearch/Sum_of_Matrix_After_Queries.py)

先想到用 list 来储存每一列每一行最后更新的数和更新顺序，然后每一列二分找这一列里在当前列顺序之前更新的行数，然后这些行被列覆盖，剩下的保持行的数。

#### [2817. Minimum Absolute Difference Between Elements With Constraint](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/), [Solution](BinarySearch/Minimum_Absolute_Difference_Between_Elements_With_Constraint.py)

从第 x 位开始，每一步把他之前的第 x 个元素放到 sortedlist 里。这样可以保证轮到每个元素的时候，他 x 位之前的数都在 sortedlist 里。然后每一步再 sortedlist 里二分找离当前元素最近的元素。因为加元素的方式，保证了里面所有元素都离当前元素至少 x 位。然后比较二分出来的位置上的元素和当前元素的差，并更新当前的最小差。这里用了 sortedcontainers，而且 sortedcontainers 里的结构可以直接 call bisect_left 函数。

#### [Snowflake Perfect Pairs](https://leetcode.com/discuss/interview-question/1781247/TuSimple-or-OA-or-Perfect-Pairs)

条件 2 总是满足的，而条件 1 等价于|x| <= |y|, |y| <= 2|x|。所以先取绝对值，排序，然后从前往后对每个下标 i，找到 i < j, nums[j] <= 2nums[i]的最大的 j。从 i + 1 到 j 都是满足和 i 的 perfect pair。

#### [Snowflake Cross the Threshold](https://www.1point3acres.com/bbs/thread-931627-1-1.html)

可以用二分查找答案范围，也可以先排序然后递增 barrier 来逐步减小 sum。都是 nlogn。

#### [Snowflake Maximize Array Value](https://leetcode.com/discuss/interview-question/2140142/Snowflake-OA-or-Maximize-Array-Value), [Solution](https://maplezoo.notion.site/Maximize-Array-Value-4c8551f092e94daf8b7aca3228e9c81a), [Solution](BinarySearch/Maximize_Array_Value.java)

从 0 到最大值二分查找。每轮验证当前的 max 是否可以达到。i 从后往前，diff = Math.max(nums[i] + diff - max, 0);这里如果 nums[i] <= max 就没问题，否则作为 diff 传到下一个数，这个 diff 需要在之后被抹平。如果到 0 都没被抹平就说明当前的 max 无法达到；diff 最后为 0 则说明可以达到。

#### [Snowflake Largest Sub-grid](https://leetcode.com/discuss/interview-question/1215695/Microsoft-OA-Largest-Sub-grid), [Solution](https://maplezoo.notion.site/Largest-subgrid-c0b3d259c7d84bd58a93866497b2a3db)

在最小 max，1x1，和最大 max，nxn 里面二分，求满足条件的最大 kxk。

#### [Snowflake Server Selection](https://leetcode.com/discuss/interview-question/2594968/Snowflake-or-OA-or-Server-Selection), [Solution](https://leetcode.com/discuss/interview-question/2594968/Snowflake-or-OA-or-Server-Selection)

对答案二分。二分的每一步中假设现在是 x，首先过一遍 vulnerability，把大于等于 x 的元素标位 1，其他是 0。然后再过一遍，记录每一行 1 的个数。这个和前面可以合成一步。再对每一列，记录第一个为 1 的行的 index。如果有一列找不到说明不管怎么取这一列的 min 都小于 x，往左二分。都找到之后如果行 index 的数量小于 M 说明可以，向右二分，包含当前 x。如果 index 数等于 M 但是其中存在一行，1 的 count 数大于 1，说明有一行可以覆盖多列，一样可以，向右二分。否则向左二分。

---

<div id='SlidingWindow'></div>

## Sliding Window

#### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/), [Solution](SlidingWindow/Longest_Substring_Without_Repeating_Characters.py)

记录之前每一个数的下标，以及 left。每一步如果以前记录过且在 window 内，则更新 left 到记录过的下标+1，否则不用管。然后把当前元素的下标也记录进去。最后更新 res 到当前下标 - left + 1.

#### [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/), [Solution](SlidingWindow/Minimum_Size_Subarray_Sum.py)

window 记录里面的和，大于等于 target 之后开始缩小 window 并更新最小 window 大小。

#### [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/), [Solution](SlidingWindow/Sliding_Window_Maximum.py)

要想到 maintain 一个 deque，储存当前 window 里从最大元素开始往右依次减小的下标。这样第一个下标始终是当前 window 里最大元素的下标。因为加进去一个数之后 window 里面这个数之前的元素就都没用了，所以 window 是单调的。用一个 clean 函数来维护，clean 是 O(1)的。首先从左边去掉不在 window 里的下标，然后从右边开始去掉小于当前元素的下标。因为维护前是从大到小，所以维护后也是从大到小。然后用这个 deque 遍历 nums 就行了。

#### [1100. Find K-Length Substrings With No Repeated Characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/), [Solution](SlidingWindow/Find_K-Length_Substrings_With_No_Repeated_Characters.py)

用一个 set 储存当前 window 里的元素方便快速查找，用一个 deque 按顺序储存当前 window 的元素和下标。每一步，如果 window 已经满了，丢掉最前面的，更新 window 大小；如果新元素已经在 window 里，丢掉到重复元素位置并根据最后丢掉的元素的下标更新 window 大小；最后把新的元素放进来，如果 window 是满的就 substring 数加一。

#### [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/description/), [Solution](SlidingWindow/Jump_Game_VI.py)

和 239 一样，用一个 mono deque 记录每个下标位置的最大 score，每一步更新并保持 window 单调下降，且 window 里 score 最大的在第一个。

#### [1852. Distinct Numbers in Each Subarray](https://leetcode.com/problems/distinct-numbers-in-each-subarray/description/), [Solution](SlidingWindow/Distinct_Numbers_in_Each_Subarray.py)

滑动窗口，用字典统计窗口的的数字和个数。

#### [2516. Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/), [Solution](SlidingWindow/Take_K_of_Each_Character_From_Left_and_Right.py)

直接 sliding window 就行了。。。每加进来一个就检测窗口内元素是否过多，过多就一直++左边界，不然就重复加新元素。

#### [2537. Count the Number of Good Subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/description/), [Solution](SlidingWindow/Count_the_Number_of_Good_Subarrays.py)

用 hashmap 记录当前 window 里的 good pair。然后 right 右移 hashmap 对应增加，left 左移直到 window 里 count 数小于 k。

#### [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/), [Solution](SlidingWindow/Count_Complete_Subarrays_in_an_Array.py)

统计以每个下标作为左边界的所有 complete subarray。窗口往右滑，如果当前窗口是一个 complete subarray 那么从当前窗口往右的所有 subarray 都是 complete 的。然后窗口左边右移一位，如果当前窗口不 complete 了就右移右边界直到 complete，如果直接 complete 就直接统计。

#### [2831. Find the Longest Equal Subarray](https://leetcode.com/problems/find-the-longest-equal-subarray/description/), [Solution](SlidingWindow/Find_the_Longest_Equal_Subarray.py)

先预处理，得到每个数以及包含这个数的所有区间，然后对每个数的区间用 sliding window，依次加入下一个区间直到 count 超过 k，然后就把 window 头部的区间 pop 出去。

---

<div id='TwoPointer'></div>

## Two Pointer

#### [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/), [Solution](TwoPointer/Sort_Colors.py)

可以直接用 quicksort，merge sort 之类的。还有一个 O(N)的方法，保持三个指针，p0, p2, curr。p0 左边全是 0，p2 右边全是 2，curr 是当前位置。如果当前是 0，交换 curr 和 p0。因为 curr 在 p0 右边，所以从 p0 换过来的是已经检测过的，p0 和 curr 都可以++。如果 curr 是 1 则不变。如果 curr 是 2，交换 curr 和 p2，p2--。这里因为从 p2 交换过来的没有检测过，所以 curr 不能前移，要保持在原地。

#### [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/), [Solution](TwoPointer/Two_Sum_II_-_Input_Array_Is_Sorted.py)

Two Sum 可以用 two pointer 做也可以用 hashmap 做，用 two pointer 的缺点是要先排序，优点是空间 O(1)。这里既然已经排过序了，就可以直接用 two pointer。

#### [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/), [Solution](TwoPointer/Two_Sum_IV_-_Input_is_a_BST.py)

BST 的 inorder 遍历会得到一个 nondecreasing 的序列。所以用一个 inorder+twopointer 就行了。

#### [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/description/), [Solution](TwoPointer/Boats_to_Save_People.py)

排序之后依次匹配最小的和最大的，小于等于 limit 就一起放进去，否则只把大的放进去。

#### [1099. Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/description/), [Solution](TwoPointer/Two_Sum_Less_Than_K.py)

先排序，然后用 two pointer。很简单。还可以利用题目的条件 k 在 1-1000 之间，不过这个感觉不够通用，就算了。

#### [1372. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/), [Solution](DFS/Longest_ZigZag_Path_in_a_Binary_Tree.py)

从 root 开始 DFS，可以用一个 self 全局变量记录。另外其实可以不用 memo，因为每条路只计算了一次。

#### [2576. Find the Maximum Number of Marked Indices](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/), [Solution](TwoPointer/Find_the_Maximum_Number_of_Marked_Indices.py)

先排序。因为最多有 n//2 对，所以 j 从(n + 1) // 2 开始。之后 i 从 0 开始，满足条件就 i++，否则不变。最后 i \* 2 就行。

#### [2597. The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/description/), [Solution](DP/The_Number_of_Beautiful_Subsets.py)

按除 k 的余数分类，然后在每个子集里讨论。每个子集里如果和前一个恰好差 k 就不能取，就是 house robber 问题。中间每一步乘的是 v - 1，因为考虑的是取当前元素的情况，所以减去全部不取的那个情况。同样，最后返回 res - 1 也是这样。

---

<div id='DFS'></div>

## DFS

#### [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/), [Solution](DFS/Letter_Combinations_of_a_Phone_Number.py)

简单，recursive 遍历，对前一步生成的所有组合加上这一步的数字对应的所有字母。

#### [77. Combinations](https://leetcode.com/problems/combinations/description/), [Solution](DFS/Combinations.py)

简单。下一个长度的 combination 由上一个长度加上所有可能得没用到的数组成。也可以用 recursion。

#### [79. Word Search](https://leetcode.com/problems/word-search/description/), [Solution](DFS/Word_Search.py)

从 board 的每个位置开始 dfs+backtrack 搜索 word。注意先 pre check 是否 board 里包含了 word 里的所有字母，不然会超时。

#### [133. Clone Graph](https://leetcode.com/problems/clone-graph/description/), [Solution](DFS/Clone_Graph.py)

保存一个 seen dict，然后对每个 neighbor 迭代 clone。

#### [139. Word Break](https://leetcode.com/problems/word-break/), [Solution](DFS/Word_Break.py)

用 backtrack 往下一个个查，注意要缓存不然会超时。用`@lru_cache`缓存。

#### [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/), [Solution](DFS/Course_Schedule.py)

直接检测是否有环。中途传回 True / False，方便检测到环的话快速结束。

#### [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/), [Solution](DFS/Course_Schedule_II.py)

一个拓扑排序。对每个点，如果已经标记了则跳过，如果已经临时标记了说明有环 return。都没有则给一个临时标记，然后对所有相邻的点 dfs。都 dfs 完了返回之后再去掉当前临时标记，做永久标记，然后放到拓扑序最前面。

#### [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/), [Solution](DFS/Longest_Increasing_Path_in_a_Matrix.py)

dfs 返回从当前坐标开始的最长路径长度，用一个 path_length 来记录已计算过的格子

#### [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/description/), [Solution](DFS/Concatenated_Words.py)

直接 dfs，对每个单词从每个下标分成两半，查找前一半和后一半是否在 words 里或者能表示成 words 里词的拼接。把 words 转换成 set，加上 memorization 来提速。

#### [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/description/), [Solution](DFS/Predict_the_Winner.py)

maxDiff 记录从这个 player 开始，他能达到的最大 difference。A 可以从左边或右边拿，A 拿了之后 B 拿，B 依然要从 B 开始最大化他的 difference。那么 A 的 difference 就是 A 拿左边或右边之后减去 B 的 maxDiff，两个里面更大的那一个。

#### [526. Beautiful Arrangement (similar to 46)](https://leetcode.com/problems/beautiful-arrangement/), [Solution](DFS/Beautiful_Arrangement.py)

T(N!), O(N)
直接 backtrack，用一个 self.count 来记录当前有效 permutation。每次 idx 到末尾就更新 count。

#### [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/), [Solution](DFS/Number_of_Provinces.py)

直接 dfs。检测连通分量个数。

#### [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/), [Solution](/DFS/Partition_to_K_Equal_Sum_Subsets.py)

T($k*2^N$), O(N)

先检测整体和是否能被 k 整除，可以的话用 backtrack。每次往当前和里加一个元素，如果超过 target_sum 就直接返回，如果等于就 count += 1 然后当前和清零继续下一次 backtrack，如果小于就依次往当前和里加入下一个元素并 backtrack。注意就算从当前元素，不从头开始 backtrack，且预先排序，依然在 python 上超时。

#### [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/description/), [Solution](DFS/Longest_String_Chain.py)

从长到短倒着 dfs。这样可以不用每个字母每个位置都插入再尝试。

#### [2538. Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description/), [Solution](DFS/Difference_Between_Maximum_and_Minimum_Price_Sum.py)

用两次 dfs，第一次以 0 为 root，算出每个节点的最大和；第二次从 0 开始，往下 dfs 的时候传一个 parent_contribution，即在每个节点的 parent 方向的最大路径和。为了计算 parent_contribution，在每个节点算出包含他自己的 parent_contribution 在内的前两大的路径和。这样在所有子节点上，如果碰到了最大路径的节点，就把第二大的作为 parent_contribution 传入。

#### [2811. Check if it is Possible to Split Array](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/description/), [Solution](DP/Check_if_it_is_Possible_to_Split_Array.py)

dp，对每个子列[i:j]检查[i:j - 1]或[i + 1:j]是否满足当前条件且本身可以被 split。

---

<div id='BFS'></div>

## BFS

#### [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/), [Solution](BFS/Binary_Tree_Level_Order_Traversal.py)

简单，用两个 q 交替记录当前层和下一层的 node，然后每层的 val 依次 append 到一个 list 里。

#### [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/description/), [Solution](BFS/Word_Ladder_II.py)

首先建一个 interword 的字典，保存这些 interword 可以通向哪些 word。然后从 begin word 开始 bfs。TLE 了。

#### [127. Word Ladder](https://leetcode.com/problems/word-ladder/description/), [Solution](BFS/Word_Ladder.py)

因为只要找到 endWord 就行，所以可以直接 bfs+visited，不管中间是否有路径重叠。注意用一个 interWord 保存中间态，预处理 wordList 找到所有中间态，然后每一步转换成中间态之后再查找这个中间态可以到达哪些词。

#### [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/description/), [Solution](BFS/Walls_and_Gates.py)

基本 bfs，从每个 gate 出发 bfs 并记录经过的格子。

#### [317. Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/description/), [Solution](BFS/Shortest_Distance_from_All_Buildings.py)

可以从每个空地开始 bfs 到每个 building，或者从 building 开始 bfs 到空地。从 building 开始还可以每一步只 bfs 之前能 bfs 到的那些空格，可以更快。从空地开始的会超市。

#### [542. 01 Matrix](https://leetcode.com/problems/01-matrix/description/), [Solution](BFS/01_Matrix.py)

先把所有 0 的距离置为 0，然后从 0 开始出发 bfs，把剩下的所有距离安上。

#### [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/), [Solution](BFS/Maximum_Width_of_Binary_Tree.py)

bfs，每一层计算每个点的 index，这一层过完之后更新最大 index 差，即宽度。

#### [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/description/), [Solution](BFS/Number_of_Enclaves.py)

和昨天的一样，不过可以从边界开始 bfs，然后统计没有被 bfs 到的 1 的个数。

#### [1293. Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/), [Solution](BFS/Shortest_Path_in_a_Grid_with_Obstacles_Elimination.py)

bfs，queue 里每一步记录 state 包含当前位置和还能去掉几个 obstacle。用 set 记录这个 state 保证不重复。

#### [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/), [Solution](BFS/Reorder_Routes_to_Make_All_Paths_Lead_to_the_City_Zero.py)

简单 bfs。先记录所有单向边并同时保存双向边。然后从 0 出发 bfs 延双向边走，每走一步判断当前对应的单向边是否指向 0，不指向的话就 count + 1。

#### [2577. Minimum Time to Visit a Cell In a Grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/), [Solution](BFS/Minimum_Time_to_Visit_a_Cell_In_a_Grid.py)

bfs + heap。依次把没去过的点放到 heap 里面，注意四周的点的到达时间取 max(time + 1, grid[nrow][ncol] + wait)。

---

<div id='DP'></div>

## DP

#### [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/description/), [Solution](DP/Unique_Paths_II.py)

简单 dp，根据当前位置是否有障碍物决定返回上方和左方的和或是直接 0.

#### [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/), [Solution](DP/Unique_Paths.py)

简单 dp。

#### [72. Edit Distance](https://leetcode.com/problems/edit-distance/), [Solution](DP/Edit_Distance.py)

明明是 DP 不是 DFS 啊。如果作 change，看看当前位置的 character 是否一样。如果作 delete，在 dp[i-1][j]上加 1。如果作 insert，在 dp[i][j-1]上加 1。取三个里面最小的。

#### [87. Scramble String](https://leetcode.com/problems/scramble-string/description/), [Solution](DP/Scramble_String.py)

可以用 recursion，很简单，不过要加 cache。也可以手动加。另外也可以三维 bottom to top dp，dp[length][i][j]表示从 s1 第 i 位开始，s2 第 j 位开始，长为 length 的子串是否 scramble。

#### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/description/), [Solution](DP/Interleaving_String.py)

用的算是 brute force+cache，但其实可以用 DP。dp[i][j]储存能否用 s1[:i+1]和 s2[:j+1]interleave 出 s3[:i+j+1]。

#### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock.py)

简单，甚至不能称为 dp，保存到目前为止的最小值，取当前价格和当前最小值的差并更新当前最大值。

#### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_II.py)

因为可以卖无限次，所以只要后一天比前一天价格高就可以买进卖出。

#### [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_III.py)

dp[k][i]是最多进行 k 次交易，最后一次最多在 prices[i]卖出，的最高总收益。所以如果最后一次不在 prices[i]卖出，就等于 dp[k][i - 1]；如果卖出，就等于 prices[i] - prices[j] + dp[k][j - 1] for j = 0, ..., i。因为只有 j 在变，所以等价于求 min of prices[j] - dp[k][j - 1]。因为这里只有 j 在变，所以直接用 min(currMin, prices[i] - dp[k][i - 1])就行了，因为比 i 小的已经在前面算过了，这里只要算当前值会不会更小就行。

#### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/), [Solution](DP/Maximum_Product_Subarray.py)

每一步记录当前为止的最小值和最大值，并更新当前最大值。

#### [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_IV.py)

和 123 一模一样，就是推广到最多进行 k 次交易。另外注意这里允许在同一天先买进再卖出。

#### [198. House Robber](https://leetcode.com/problems/house-robber/description/), [Solution](DP/House_Robber.py)

最简单的一维 dp。

#### [213. House Robber II](https://leetcode.com/problems/house-robber-ii/description/), [Solution](DP/House_Robber_II.py)

用原版 house robber 作辅助函数，根据拿不拿 nums[-1]分两种情况，分别做两次 dp。

#### [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/), [Solution](DP/Longest_Increasing_Subsequence.py)

dp[i] = 以第 i 个元素结尾的最长递增子序列。di[i] = max(dp[j] + 1) if dp[i] > dp[j] for j < i.

#### [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py)

建一个两行的 dp，第一行表示在当前位置没有卖出，第二行表示在当前位置卖出了。迭代思路和 k 次交易的一样，用一个 currMin 来减少运算。最后取两行末尾的最大值。

#### [322. Coin Change](https://leetcode.com/problems/coin-change/description/), [Solution](DP/Coin_Change.py)

很标准的 dp 题，对用到的硬币数量和 amount 大小进行 dp。

#### [337. House Robber III](https://leetcode.com/problems/house-robber-iii/description/), [Solution](DP/House_Robber_III.py)

recursion + memorization。根据拿不拿 root 分类。加上点边界条件就行了。

#### [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/),[Solution](DP/Combination_Sum_IV.py)

对 target 进行 dp，以 nums 里的每个数 num 作结尾都是不同的组合，然后 dp(target-num)。用 cache 加记忆。

#### [403. Frog Jump](https://leetcode.com/problems/frog-jump/description/), [Solution](DP/Frog_Jump.py)

不是最优解，差不多是 brute force+cache。可以用 DP。用一个字典储存 key:value, key 是每个位置，value 是能到这个位置的 jump 的长度的集合。最后如果最后一个位置在字典里，就说明可以跳到这里，否则不可以。

#### [418. Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/description/), [Solution](DP/Sentence_Screen_Fitting.py)

dp 从第 i 个 word 开始，一行能放下几次 sentence。同时返回下一行的开始 index。一次都放不完就是 0。这样没影响，因为一行能放下多次的话可以正确记录，一行一次都放不完的话后面总有可以放完，在后面再行数+1。

#### [494. Target Sum](https://leetcode.com/problems/target-sum/description/), [Solution](DP/Target_Sum.py)

用的 recursive dp，加一个字典 memorization。还可以优化从传数组变成传下标。

#### [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/), [Solution](DP/Longest_Palindromic_Subsequence.py)

dp，每次比较 i，j 和 i + 1， j - 1 加上头尾是否相等、i + 1， j、i， j - 1 之间的最大值。

#### [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/), [Solution](DP/Coin_Change_II.py)

每个 coin 有两种可能，用到或者不用到。所以对 coin 的 index 和 amount 做 dp，每次考虑用到或者不用到这个 coin 的情况。

#### [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/), [Solution](DP/Course_Schedule_III.py)

先按结束时间排序，然后依次处理。维护到当前位置的上的最多的课，每个课的时长，和总时长。新的课来了之后，如果在当前时间直接上不超过 lastDay，就直接放进 heap 里；如果超过了，duration 大于之前的所有课的最大时长的话，不能放，否则无法维护是上的最多的课；如果小于之前的最大时长，则直接替换，可以维护是上的最多的课。因为是按结束时间排序，所以可以直接放进去替换。因为用了 heap，所以总时长和之前上的课的时长也可以快速维护。

#### [664. Strange Printer](https://leetcode.com/problems/strange-printer/description/), [Solution](DP/Strange_Printer.py)

dp[i][j]表示从 s 第 i 个到第 j 个的 substring 的最少 print 数。每有一个新的进来，如果和前一个一样 dp 就也一样。如果不一样那就有两种方法。一个直接在 dp[i][j - 1]基础上多 print 一次，一个从前一个相同字符开始覆盖到这里，然后重新 print 中间的部分。每一步对前面的所有元素都判断一次。

#### [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/), [Solution](DP/Number_of_Longest_Increasing_Subsequence.py)

简单 dp，不过 edge case 弄了一会。用 dp 记录数组(l, s)，l 是以当前元素为结尾的最长递增序列的长度，s 是以当前元素为结尾的最长递增序列数。每个新元素过一遍前面的所有元素，如果前面的比当前的小那就是递增序列，根据前面的长度决定是否是最长递增序列以及是否加到现在的计数里去。

#### [688. Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/description/), [Solution](DP/Knight_Probability_in_Chessboard.py)

用棋盘记录每一步在每个格子上的概率。每一步更新整个棋盘所有格子的概率。最后对最后一步之后的整个棋盘上的概率求和。

#### [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/description/), [Solution](DP/Cherry_Pickup.py)

第二次不用从 n-1, n-1 往回走了，直接从 0, 0 往右下出发两个路径，然后三维 dp，dp[r1][c1][r2]，然后让两个点在同一反对角线上，这样 c2 = r1 + c1 - r2。

#### [799. Champagne Tower](https://leetcode.com/problems/champagne-tower/description/), [Solution](DP/Champagne_Tower.py)

其实是模拟，记录每个杯子里流过的总量，超过 1 就往下面倒(总量 - 1) / 2。

#### [808. Soup Servings](https://leetcode.com/problems/soup-servings/description/), [Solution](DP/Soup_Servings.py)

dp 用一个 helper function 分别返回 A 先 empty 的概率和同时 empty 的概率。注意 n 过大时因为 serve 的方式不对称所以 A 先 empty 的概率接近 1。所以 n 过大时直接返回 1 就行了。

#### [920. Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/description/), [Solution](DP/Number_of_Music_Playlists.py)

dp 题最重要要有思路。dp[i][j]表示要放 i 首歌，有 j 个 unique 歌曲的方法数。如果第 i 个歌是新的，那么 dp[i][j] = dp[i - 1][j - 1] _ (n - j + 1)，其中 n - j + 1 表示除了已经有的 j - 1 首歌之外，剩下的 n - (j - 1)首歌。如果第 i 个歌已经放过了，那么 dp[i][j] += dp[i - 1][j] _ (j - k)，表示已经放过的里面后 k 首不能选，因为要放 k 首其他歌之后才能重新放。

#### [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/description/), [Solution](DP/Minimum_Cost_For_Tickets.py)

基本 dp，根据在第 i 天用 1/7/30pass 来分类，取里面的最小的。另外注意 bisect.bisect_left 和 bisect.bisect，第一个是使找 a[:i] < x，a[i:] >= x 的下标 i，第二个是 a[:i] <= x，a[i:] > x 的下标 i。

#### [1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/description/), [Solution](DP/Valid_Palindrome_III.py)

直接 dp，能不能变成 palindrome 取决于变成 palindrome 的最小次数是否小于 k。dfs(i, j)如果 s 的 i 和 j 相等，则等于 dfs(i+1, j-1)。否则说明 i 或者 j 之间要去掉一个，就等于 1+min(dfs(i+1, j), dfs(i, j-1))。

#### [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/), [Solution](DP/Maximum_Profit_in_Job_Scheduling.py)

直接 dp，用 recursion+lru_cache 可以直接过，用 memorization 的话就必须用二分搜索。dp(i) = dp(i+1)或者对第 i 个工作结束时间之后的所有工作 j，profit[i]+dp(j)中最大的那个。

#### [1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/), [Solution](DP/Minimum_Number_of_Taps_to_Open_to_Water_a_Garden.py)

dp[i]表示从 0 到 i 需要的最少 tap 数。然后遍历每个 tap 考虑用到这个 tap 的情况下，用这个 tap 覆盖范围内的 dp[j]来更新这个 tap 的最远覆盖点处的 dp。就是每个 dp[j] + 1 里面最小的那个。

#### [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/), [Solution](DP/Minimum_Difficulty_of_a_Job_Schedule.py)

直接 dp，dp(i, d)表示从第 i 个工作开始，还剩下 d 天。dp(i, d)等于在当天安排从 i 到 j-1 的工作，然后剩下的 d-1 天做 j 之后的工作，即 dp(j, d-1)，对所有 j > i 里面最小的那一个。用 lru_cache 减少时间。

#### [1444. Number of Ways of Cutting a Pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/), [Solution](DP/Number_of_Ways_of_Cutting_a_Pizza.py)

3d 的 DP。能想到 3d 的话就还好。看起来 dp 还是专门留一行空的出来比较好，这样就不用初始化了。先预处理，统计每个位置 i，j 右下方的苹果数。然后从 i，j 出发，按行和按列切，如果被切下来的部分和剩下的部分都有苹果就更新 res。

#### [1639. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/), [Solution](DP/Number_of_Ways_to_Form_a_Target_String_Given_a_Dictionary.py)

先找出每个下标上每个字母出现的次数，然后 dp。dp(t, n)对应用 word[:n]拼出 target[:t]的方法数。

#### [2222. Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/description/), [Solution](DP/Number_of_Ways_to_Select_Buildings.py)

dp[k][j]为在 s[:i + 1]中选择长度为 k 的挑选方法数。同时分别保存其中以'0'和'1'结尾的方法数。dp[k + 1[j]考虑是否以 s[j]结尾，不结尾直接用前一个，结尾再加上 dp[k][j - 1]里面结尾元素和 s[j]不同的方法数。

#### [2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/description/), [Solution](DP/Substring_With_Largest_Variance.py)

用 dp，相当于 max subarray 的一个变体。分别判断所有两个字母的组合，最多 25x26 种组合，每个组合花 O(n)的时间。判断当前字母并增减 max_subarray 后，根据后续是否无任何字母或两个字母都有还是其他，判断是中断本次循环还是重置窗口还是继续当前循环。

#### [2291. Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks/description/), [Solution](DP/Maximum_Profit_From_Trading_Stocks.py)

一个 budges \* n 的 dp。有一些 edge case，像初始化，在有足够钱且当前收益为正的情况下才进行交易等。

#### [2305. Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/description/), [Solution](DP/Fair_Distribution_of_Cookies.py)

DP+bitmask。几个操作 1 << n 是 bit 往左移 n 位。a & b，a ^ b。用整数表示一个组合，他的 bit 表示 1 的位置说明取到这个位置的元素。对 mask 求和里面 mask & (1 << i)表示 mask 里第 i 个位置是否为 1.然后从 bagMask 开始往下取 mask = (mask - 1) & bagMask。因为&操作只会把数变小，所以是从大往小取。每轮里面取 res = min(res, max(sum1, sum2))，因为是要取最小的最大值。sum1 = sumMask(mask)是这个 mask 单独分给一个人的和，sum2 = unfairness(k - 1, bagMask ^ mask)是 bagMask 去掉 mask 后剩下的 cookie 分给其他人的最大值。

#### [2444 Count Subarrays With Fixed Bounds](https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/), [Solution](DP/Count_Subarrays_With_Fixed_Bounds.py)

先过一遍 nums，记录每个坐标前最近的等于 minK，等于 maxK，超出范围的值的坐标，记为 prev[0], prev[1], prev[2]。然后 dp。dp[i] = dp[i-1]，如果 nums[i]没超出范围，那么 dp[i]再加上 prev[0], prev[1]里更小的那个到 prev[2]的距离。如果是负的就不加。

#### [2369. Check if There is a Valid Partition For The Array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/), [Solution](DP/Check_if_There_is_a_Valid_Partition_For_The_Array.py)

基础 dp，dp[i]取决于 i 之前的两个或三个数字是否满足条件以及更之前的 dp 是否 valid。

#### [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/), [Solution](DP/Maximum_Number_of_Non-overlapping_Palindrome_Substrings.py)

dp 检查到 i 下标之前的子串，里面长度大于 k 的回文串的最大长度。注意这里对以 i-1 结尾的子串，只用检查长度为 k 和长度 k-1 的就行，更前面的不用检查。

#### [2518. Number of Great Partitions](https://leetcode.com/problems/number-of-great-partitions/description/), [Solution](DP/Number_of_Great_Partitions.py)

dp[i][j]表示在 nums[:i]中和为 j 的子集数。j 从 0 到 k - 1，dp[-1][j]就是 nums 中和为 0 到 k - 1 的所有子集数。在所有 2^n 种组合中减去第一组的和及第二组的和小于 k 的子集数。关键要能想到这么算。

#### [2547. Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/description/), [Solution](DP/Minimum_Cost_to_Split_an_Array.py)

切木条的变种，区别是切木条里面相应长度木条的价格都给出来了，这里要先算一下每个 nums[i:j]的 cost 并记录。

#### [2684. Maximum Number of Moves in a Grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/), [Solution](DP/Maximum_Number_of_Moves_in_a_Grid.py)

基本 dp，从后往前 dp。每次看前一列的上下三行。

#### [2707. Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/description/), [Solution](DP/Extra_Characters_in_a_String.py)

从每一个下标开始 dp。先初始化成 dp(start + 1) + 1 就是不用当前字母，当前字母就是 extra 字母了。然后 recursion 对后面每一个下标看从当前到后面在不在 dictionary 里，然后更新 res。

#### [2742. Painting the Walls](https://leetcode.com/problems/painting-the-walls/description/), [Solution](DP/Painting_the_Walls.py)

dp，dp[i][j]表示第 i 个 wall 用 paid 来做的情况下，完成 j 个 wall 的最低 cost。可以只用一维来记录。每个 dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])，这里等号右边的 dp[j]表示上一步的结果。取这个和使用第 i 个 paid 的情况下，也就是用 cost[i]。用了 cost[i]会占用 time[i]的时间，所以可以完成当前的 wall 以及另外 time[i]个用 free 完成的 wall。去掉这么多 wall，剩下的最低 cost 再加上 cost[i]，和上一步的取更低的那一个，更新下一步。

#### [2750. Ways to Split Array Into Good Subarrays](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/), [Solution](DP/Ways_to_Split_Array_Into_Good_Subarrays.py)

dp 题有思路就好做。dp[i]如果是 0 就没有新的 split 方法，直接和前一个一样；如果是 1 那就可以有新的从前一个一后面的那个 0 开始一直到这个 1 前面的那个 0 那么多种方法数，这些加起来。比如 10000 后面来一个 1，那么就有 00001，0001,001,01,1 这些新的 split。

#### [2830. Maximize the Profit as the Salesman](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/description/), [Solution](DP/Maximize_the_Profit_as_the_Salesman.py)

周赛的时候没思路，其实不难，按照结束的 house 分个类，然后对每个结束的 house 做 dp。先初始化成 dp[i - 1]因为可以完全不选以 i 结尾的 offer。然后对每个以 i 结尾的 offer，看 dp[start] + gold 和 dp[i]的大小。

#### [Snowflake String Pattern](https://www.geeksforgeeks.org/number-of-distinct-words-of-size-n-with-at-most-k-contiguous-vowels/), [Solution](DP/String_Pattern)

dp[i][j]表示长度为 i 的 string，最后 j 位是元音，的组合数。对每个 i，dp[i][0]由 i - 1 的行和初始化。之后根据 j 和 i 的相对大小来判断状态转移方程。可以只保留一行作为 dp 储存，因为只用到了上一行的 dp。

#### [Snowflake String Formattion](https://www.1point3acres.com/bbs/thread-929005-1-1.html)

dp[i][j] = 到 target 的第 i 个字母，使用的字母到所有 word 到第 j 个为止。每一个 i，j < i 为 0，j = i 等于 dp[i - 1][i - 1] _ target[i]在第 j 个位置出现的次数。j > i，等于 dp[i - 1][k] _ target[i]在第 k 个位置出现的次数，对 k 从 i - 1 到 j 求和。

#### [Snowflake Palindrome Sequence](https://leetcode.com/discuss/interview-question/algorithms/202924/ascend-online-assessment-product-of-palindromes#:~:text=Palindromic%20subsequences), [Solution](https://stackoverflow.com/questions/53663721/find-the-maximum-product-of-two-non-overlapping-palindromic-subsequences), [Solution](DP/Palindrome_Sequnce.java)

先 dp，找出从 i 到 j 中间的最长 palindrome 的长度。注意 dp 是在每个对角线上 dp。然后以每个下标为分界点，求分界点左右乘积的最大值。

#### [Snowflake Task Scheduling](https://leetcode.com/discuss/interview-question/2775415/SnowFlake-OA), [Solution](DP/Task_Scheduling.java)

dp(i, j)表示第 i 个 task 时，还剩 j 个 free time 的 min cost。每次考虑 task i 放 paid 还是 free server，paid 就 cost += c[i]，j += time[i]，free 就 j -= 1 最后 i = n 的时候如果 j < 0 就说明这一列不可行，直接返回 inf。

#### [Snowflake Paths to a goal](https://zany-fluorine-852.notion.site/snowflakes-oa-f32a12c872344de98837ac986abc850e), [Solution](DP/Paths_to_a_Goal)

dp[i][j]使用到 s[i]为止的 rl，到达位置 j 的不同方法数。每一步减去上一个和当前相同方向的方法数，即 dp[pre_same[i]][j +- 1]。

---

<div id='Greedy'></div>

## Greedy

#### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/description/), [Solution](Greedy/Jump_Game_II.py)

其实也算 bfs 吧，从每个点记录所有能跳到的点，直到碰到终点。

#### [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort/description/), [Solution](Greedy/Wiggle_Sort.py)

首先可以直接排个序，然后每隔一位交换相邻数。或者可以每一位上根据奇偶看跟下一位的大小关系来决定是否和下一位交换。

#### [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/), [Solution](Greedy/Non-overlapping_Intervals.py)

先按结束时间排序，然后依次检测，如果下一个的开始时间大于等于前一个的结束时间，就不去掉，否则去掉这一个。这样相当于在两个重叠的里面保留了结束时间更早的那个，这样就给后面的留了更多空间。

#### [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/description/), [Solution](Greedy/Validate_Stack_Sequences.py)

依次 push，只要 stack 末尾和 pop 匹配上就 pop，直到不匹配，然后 push 下一个。最后检测 stack 是否为空。

#### [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/description/), [Solution](Greedy/Two_City_Scheduling.py)

因为每个人都必须被分到一个 city 去，所以算一下每个人的 costA - costB 再排序，前 n 个人就去 a，剩下的去 b。

#### [1402. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/description/), [Solution](Greedy/Reducing_Dishes.py)

排序。0 和正数肯定要选，这之后每加一个负数，相当于增加前面所有正数的和，并减去到目前为止加进来的所有负数以及当前这个负数。所以从绝对值小到大开始对负数求和，直到减去的量大于等于正数的增量为止。记录下标，并计算从这个下标开始取的结果。

#### [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/description/), [Solution](Greedy/Path_With_Minimum_Effort.py)

用了类似 Dijrastra 的思路，每一步把相邻没访问过的加到 heap 里，然后取当前所有 heap 里 effort 最小的那个。注意保存到状态包括 effort，不止位置，因为同一个位置可能从不同方向访问，effort 不一样。

#### [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/description/), [Solution](Greedy/Maximum_Running_Time_of_N_Computers.py)

先排序，然后把最大的 n 个电池分配出去。把剩下的加起来，然后对使用中的那 n 个电池从小到大，依次用剩余的电池把第 0 到第 i 个电池的容量补到第 i + 1 个那么多。这样电脑就可以运行 i+1 那么长时间。如果一直到最后还有剩余或者中间停住不能补到下一个，就把剩余的所有电量平均分配到所有电池或者前 i 个电池上。

#### [2193. Minimum Number of Moves to Make Palindrome](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/), [Solution](Greedy/Minimum_Number_of_Moves_to_Make_Palindrome.py)

只用看从末尾开始，把每个对应的字母从原始位置移动到开头的消耗就行。

#### [2366. Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/), [Solution](Greedy/Minimum_Replacements_to_Sort_the_Array.py)

从后往前，依次把每一个比后面大的元素分拆。如果当前的整除后一个就分拆成所有都和后一个一样大，或者不能整除就分成比整除向下取整多一个，就是尽量少的分拆但是每一个都比后面的小。

#### [2573. Find the String with LCP](https://leetcode.com/problems/find-the-string-with-lcp/description/), [Solution](Greedy/Find_the_String_with_LCP.py)

greedy 的根据 lcp 依次填满 res 列表，如果用到的字符数超过 26 就返回''，如果遇到已经填过的就跳过。然后再循环一次检查生成的 res 是否符合 lcp。一个个位置对应检查太慢了，所以用 lcp[i][j]和 lcp[i + 1][j + 1]之间的关系来检查。如果 res[i] == res[j]那么 lcp[i][j] = lcp[i + 1][j + 1] + 1。最后根据 res 拼接出答案。

#### [2589. Minimum Time to Complete All Tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description/), [Solution](Greedy/Minimum_Time_to_Complete_All_Tasks.py)

按结束时间排序。这样从结束时间开始往前安排 task，可以让后面的 task 最大化利用前面的时间。然后后面每次过一遍 start 到 end，去掉已经安排过的时间点，然后再从后往前把剩下的时间安排完。

#### [2611. Mice and Cheese](https://leetcode.com/problems/mice-and-cheese/description/), [Solution](Greedy/Mice_and_Cheese.py)

总和 = sum ai + sum bj 其中 I 大小为 k = sum ai - sum bi + sum b 这里 sum b 是直接求和，所以是固定值，只需要最大化 sum ai - sum bi，就是算一下差值，取最大的 k 个就行了。

#### [2800. Shortest String That Contains Three Strings](https://leetcode.com/problems/shortest-string-that-contains-three-strings/description/), [Solution](Greedy/Shortest_String_That_Contains_Three_Strings.py)

枚举所有 string 的组合，然后写一个 helper 找出两个 string 能重叠的最小 super string。然后求 super(a, b)，返回的 string 再和 c 求一次 super。返回所有这些 33super 里最小的那个。

---

<div id='SQL'></div>

## SQL

#### [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/description/), [Solution](SQL/Combine_Two_Tables.py)

基本 sql 语法，select join。

#### [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/), [Solution](SQL/Second_Highest_Salary.py)

先找到最大值，然后以这个为条件，在小于他的值里面再找最大值。

#### [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/description/), [Solution](SQL/Nth_Highest_Salary.py)

创建函数的语法，create function 函数名（变量名 变量类型） return 返回类型，begin end，中间 return（），括号里写查询语句。limit x，y 表示从下标 x 开始取 y 个。

#### [178. Rank Scores](https://leetcode.com/problems/rank-scores/description/), [Solution](SQL/Rank_Scores.py)

重命名一个叫 S1，从里面选两列，一个 score，另一个是 rank。rank 是另一个 distinct copy，S2 里面每个行大于等于 S1 的个数。

#### [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/description/), [Solution](SQL/Consecutive_Numbers.py)

做三个 copy，选择里面 id 依次加一且 num 相等的 distinct 的 num 的个数。

#### [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/), [Solution](SQL/Employees_Earning_More_Than_Their_Managers.py)

建两个 copy，然后比较他们的 salary，且 e1 的 manageID 等于 e2 的 id。

#### [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/), [Solution](SQL/Duplicate_Emails.py)

where 用在输出结果之前，用来约束结果；having 用在输出结果之后，用来筛选结果。having 通常在 group by 之后。

#### [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/description/), [Solution](SQL/Customers_Who_Never_Order.py)

注意用选出来的表来看 in。

#### [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/description/), [Solution](SQL/Department_Highest_Salary.py)

从按 department id 拼起来的表里取 department name，employee name，employee salary。取的行要满足 department id 和 salary 的组合是 department 的最大 salary。

#### [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/), [Solution](SQL/Department_Top_Three_Salaries.py)

从拼起来的表里面，选出那些在同样的 id 里面，大于该项的不超过三个的那些项。

#### [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/), [Solution](SQL/Delete_Duplicate_Emails.py)

选两个 copy，删掉第一个里面的所有列，如果 email 相同且 id 大于第二个里的。

#### [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/description/), [Solution](SQL/Rising_Temperature.py)

也可以用 join。另外比较日期大小应该用 DATEDIFF。

#### [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/description/), [Solution](SQL/Game_Play_Analysis_I.py)

简单，用 MIN 函数。

#### [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/), [Solution](SQL/Managers_with_at_Least_5_Direct_Reports)

注意别名要在括号外面。

#### [574. Winning Candidate](https://leetcode.com/problems/winning-candidate/description/), [Solution](SQL/Winning_Candidate.py)

取第几大的用 order by 之后 limit 来取。

#### [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/description/), [Solution](SQL/Employee_Bonus.py)

直接用 outer join 会报错，必须 left 或者 right。

#### [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/description/), [Solution](SQL/Find_Customer_Referee.py)

mySQL 有三个逻辑值，TRUE, FALSE, UNKNOWN。只有 TRUE 会被 where 返回。所有和 null 比较的都是 UNKNOWN，不会被返回。所以要额外加一个判断 IS NULL。

#### [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/), [Solution](SQL/Customer_Placing_the_Largest_Number_of_Orders.py)

先 group 了再 order。

#### [595. Big Countries](https://leetcode.com/problems/big-countries/description/), [Solution](SQL/Big_Countries.py)

直接选。

#### [607. Sales Person](https://leetcode.com/problems/sales-person/description/), [Solution](SQL/Sales_Person.py)

join 选出 order 里面 company 为 RED 的那些的 sales_id，然后在 salesperson 里面找不在这些 id 里面的人。

#### [608. Tree Node](https://leetcode.com/problems/tree-node/description/), [Solution](SQL/Tree_Node.py)

可以用 union 把三个情况拼起来，也可以用 case when then 来作为选出来的那个 column。

#### [627. Swap Salary](https://leetcode.com/problems/swap-salary/description/), [Solution](SQL/Swap_Salary.py)

条件语句，case when condition then result 可以多个 when then，最后 end 结束。

#### [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/), [Solution](SQL/User_Activity_for_the_Past_30_Days_I.py)

注意判断大小不能用连续不等号。日期函数是 DATEDIFF。

#### [1148. Article Views I](https://leetcode.com/problems/article-views-i/description/), [Solution](SQL/Article_Views_I.py)

基本 select。

#### [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/description/), [Solution](SQL/Group_Sold_Products_By_The_Date.py)

GROUP_CONCAT 可以返回用逗号连接的字符串。

#### [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description/), [Solution](SQL/Patients_With_a_Condition.py)

用 LIKE 进行字符串匹配。sql 里字符串用单引号，%表示任意字符。

#### [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/), [Solution](SQL/Customer_Who_Visited_but_Did_Not_Make_Any_Transactions.py)

选出在 visit 但不在 transactions 里面的那些 visit id，然后取对应的 customer id，count，group by customer id。

#### [1667. Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/), [Solution](SQL/Fix_Names_in_a_Table.py)

CONCAT 函数连接字符串，SUBSTRING(string, startIndex, length of substring)取子串。注意 startindex 从 1 开始。

#### [1693. Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/description/), [Solution](SQL/Daily_Leads_and_Partners.py)

group by 可以按多个关键字 group。

#### [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/description/), [Solution](SQL/Find_Followers_Count.py)

简单。

#### [1741. Find Total Time Spent by Each Employee](https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/), [Solution](SQL/Find_Total_Time_Spent_by_Each_Employee.py)

select 列的时候可以直接做计算。然后求 sum。

#### [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/), [Solution](SQL/Recyclable_and_Low_Fat_Products.py)

easy，直接 select。

#### [1795. Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/description/), [Solution](SQL/Rearrange_Products_Table.py)

用字符串建立新 column。然后把三个表 UNION 起来。

#### [1873. Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/description/), [Solution](SQL/Calculate_Special_Bonus.py)

用 IF(conditaion, if true, else)的函数可以直接选出一列

#### [1890. The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/description/), [Solution](SQL/The_Latest_Login_in_2020.py)

用 MAX。YEAR 可以取出 date 里的年份。

#### [1965. Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/description/), [Solution](SQL/Employees_With_Missing_Information.py)

left join 之后用 where 筛选里面没有的 employee_id。

---

<div id='OOD'></div>

## OOD

#### [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/description/), [Solution](OOD/Robot_Room_Cleaner.py)

往前走，碰到墙或者已经 visit 过的就右转，四个方向都完了就返回上一个 cell。需要另外写一个 goBack 和 dfs 函数。

#### [1603. Design Parking System](https://leetcode.com/problems/design-parking-system/description/), [Solution](OOD/Design_Parking_System)

简单。
