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

#### 算法-时间复杂度

O(n): Greedy, stack, bfs, dfs
O(n logn): sort, binary, tree like, heap
O(n^2): dp, Dijkstra

---

<div id='String'></div>

## String

#### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/), [Solution](String/Longest_Palindromic_Substring.py)
从每一个下标出发，以他为中心，检查奇数长度和偶数长度发的substring是否为palindrome。还可以用dp，dp[i][j]表示s[i:j]是否是palindrome。

#### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/description/), [Solution](String/Reverse_Integer.py)
先转成str然后reverse再拼起来。用到rjust来限制不会超出64位。用到 * (1 - 2 * (x < 0))来判断正负。

#### [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/), [Solution](String/Repeated_Substring_Pattern.py)
直接对每个长度可以被s长度整除的substring复制到和s一样长然后比较是否相等。

#### [2268. Minimum Number of Keypresses](https://leetcode.com/problems/minimum-number-of-keypresses/description/), [Solution](String/Minimum_Number_of_Keypresses.py)
直接过一遍str，让频率高的放在第一个，9个button放完了就放第二个，依次。每放一个字母就count += number of ch in str * 字母在button里的位置。

#### [2288. Apply Discount to Prices](https://leetcode.com/problems/apply-discount-to-prices/description/), [Solution](String/Apply_Discount_to_Prices.py)
简单，不过注意字符串里插入变量的格式：'str%格式'%(插入的东西)

#### [2609. Find the Longest Balanced Substring of a Binary String](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/), [Solution](String/Find_the_Longest_Balanced_Substring_of_a_Binary_String.py)
先过一遍找到每个连续0,1的开始下标和连续长度，然后对所有连续0找对应的下一个相邻连续1，取res = max(res, min(连续0长度，连续1长度) * 2)。

#### [2663. Lexicographically Smallest Beautiful String](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/description/), [Solution](String/Lexicographically_Smallest_Beautiful_String.py)
不能有palindrome，就是不能有任何偶数及奇数长度的palindrome，就是不能有任意长为2或3的palindrome，就是任意连续两个或三个字符不能相同。先把字符都转成ascii码，方便递增。因为是下一个最小的，所以从后往前递增。如果一个字符递增到了k，说明要进位，就看前一个字符，当前字符先不管。如果不进位，且当前字符和前两个字符都不同，就把后面的依次放上0， 1， 2里面最小的且和前两个不同的字符。最后把数字转成字母。也算greedy吧。

#### [2734. Lexicographically Smallest String After Substring Operation](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description/), [Solution](String/Lexicographically_Smallest_String_After_Substring_Operation.py)
用数字记录字母，然后从第一个非0开始到他后面的第一个0为止，所有减1，然后再转成字母。注意这个window的边界条件。


---

<div id='List'></div>

## List

#### [163. Missing Ranges](https://leetcode.com/problems/missing-ranges/description/), [Solution](List/Missing_Ranges.py)
直接过一遍nums，如果和前一个相差大于一则ans.append一个数或一个区间。注意corner case，比如nums = []，以及lower和upper处的情况。

#### [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/), [Solution](String/Excel_Sheet_Column_Title.py)
这里因为A-Z是用1-26编号的，所以每步都减1，让余数范围变成从0-25。商的部分不变或者只是把余0的部分变成A。注意ord()可以把字符转成ascii码，chr()把ascii码转成字符。

#### [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/description/), [Solution](List/Meeting_Rooms.py)
直接过一遍，检查每个meeting的开始时间是否早于前一个的结束时间。

#### [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/), [Solution](List/Minimum_Moves_to_Equal_Array_Elements.py)
其实很简单。要想到增加n-1个数等价于减少1个数。然后算每个数跟最小值的差就行了。

#### [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/description/), [Solution](List/Next_Greater_Element_III.py)
因为从左往右递减的序列没有比他更大的，所以对这个数从右往左找，找到第一个左边比右边小的数，左边是i。从这个digit再往右走，找到最右边的比他大的digit，j，交换这两个digit。然后reverse从i + 1开始到最右边的digits。

#### [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/), [Solution](List/Degree_of_an_Array.py)
先过一遍，用字典记录每个数字的频率，第一次和最后一次出现的位置。再过一遍字典，更新max_fre和min_len。

#### [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/), [Solution](List/Partition_Array_into_Disjoint_Intervals.py)
还有个时间O(N), 空间O(1)的方法。记录currMax, possibleMax, length。如果当前的小于currMax，就说明当前元素必须在左边，所以更新currMax， possibleMax和length。

#### [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/), [Solution](List/Kids_With_the_Greatest_Number_of_Candies.py)
简单，easy题。

#### [1864. Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/description/), [Solution](List/Minimum_Number_of_Swaps_to_Make_the_Binary_String_Alternating.py)
因为只有两个字母，所以只要算其中一个字母不在正确位置上的最小位置数就行了。取两个字母里面这个数更小的那一个。

#### [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/description/), [Solution](List/Angle_Between_Hands_of_a_Clock.py)
直接算出时针和秒针的角度，然后取差的绝对值，再取跟补角里更小的那个。

#### [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/), [Solution](List/Merge_Strings_Alternately.py)
交替append list。

#### [2012. Sum of Beauty in the Array](https://leetcode.com/problems/sum-of-beauty-in-the-array/description/), [Solution](List/Sum_of_Beauty_in_the_Array.py)
先从后往前过一遍记录到每个下标为止的最小值，然后从前往后，每步记录到前一个为止的最大值，比较当前与相邻的大小以及和前面所有的最大值、后面所有的最小值的大小。

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

#### [2405. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/description/), [Solution](List/Optimal_Partition_of_String.py)
直接过一遍，用set记录，看到已经存在的就res += 1并重置set。

#### [2546. Apply Bitwise Operations to Make Strings Equal](https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/), [Solution](List/Apply_Bitwise_Operations_to_Make_Strings_Equal.py)
要发现不同组合的规则。(0, 0) -> (0, 0)，(1, 0) -> (1, 1)，(0, 1) -> (1, 1)，(1, 1) -> (1, 0)。所以只有0的情况无法改变，只要有1个1，就可以修改成任何情况。所以只要检查s和target是否同时全为0或者同时都含有1就行了。

#### [2643. Row With Maximum Ones](https://leetcode.com/problems/row-with-maximum-ones/description/), [Solution](List/Row_With_Maximum_Ones.py)
简单，每行过一遍就行了。

#### [2644. Find the Maximum Divisibility Score](https://leetcode.com/problems/find-the-maximum-divisibility-score/description/), [Solution](List/Find_the_Maximum_Divisibility_Score.py)
和前一题基本一样。

#### [2660. Determine the Winner of a Bowling Game](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/), [Solution](List/Determine_the_Winner_of_a_Bowling_Game.py)
简单，brute force就行了。

#### [2672. Number of Adjacent Elements With the Same Color](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description/), [Solution](List/Number_of_Adjacent_Elements_With_the_Same_Color.py)
每改一个数只会影响当前位置和前一个位置的adjacent element。所以就依次过一遍query，每个query只看两个位置的变化就行了。

#### [2682. Find the Losers of the Circular Game](https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/), [Solution](List/Find_the_Losers_of_the_Circular_Game.py)
简单题，直接取余数就行。

#### [2683. Neighboring Bitwise XOR](https://leetcode.com/problems/neighboring-bitwise-xor/description/), [Solution](List/Neighboring_Bitwise_XOR.py)
标得medium不过实际easy。依次根据derived判断当前位置是否取反就行了。

#### [2697. Lexicographically Smallest Palindrome](https://leetcode.com/problems/lexicographically-smallest-palindrome/description/), [Solution](List/Lexicographically_Smallest_Palindrome.py)
从中间往两边出发，每次保存对称位置上更小的那个元素，最后再把保存了的都拼起来。

#### [2698. Find the Punishment Number of an Integer](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/), [Solution](List/Find_the_Punishment_Number_of_an_Integer.py)
直接暴力解，每个数都算一遍所有组合看满不满足punishment条件。

#### [2712. Minimum Cost to Make All Characters Equal](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description/), [Solution](List/Minimum_Cost_to_Make_All_Characters_Equal.py)
分别让左半边和右半边一样，然后根据奇偶还有中间元素和中间元素两边是否相同判断最后的和。

#### [2716. Minimize String Length](https://leetcode.com/problems/minimize-string-length/description/), [Solution](List/Minimize_String_Length.py)
简单。

#### [2717. Semi-Ordered Permutation](https://leetcode.com/problems/semi-ordered-permutation/description/), [Solution](List/Semi-Ordered_Permutation.py)
简单。

#### [2735. Collecting Chocolates](https://leetcode.com/problems/collecting-chocolates/description/), [Solution](List/Collecting_Chocolates.py)
转n圈，每次更新每个位置上的最低cost加上转到这一圈需要的转圈cost，每一圈都保存当前最低总cost，最后输出。

#### [2733. Neither Minimum nor Maximum](https://leetcode.com/problems/neither-minimum-nor-maximum/description/), [Solution](List/Neither_Minimum_nor_Maximum.py)
简单，找不是最小最大值的。

#### [2749. Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/), [Solution](List/Minimum_Operations_to_Make_the_Integer_Zero.py)
根据操作次数k减去k * num2，剩下的就是由2**i组成的部分。bit_count()可以看int的二进制表示里面有几个2**i。k最小要大于等于这个bit_count()，因为这样才能组合出来；最大要小于等于num1 - k * num2，因为每次操作最少会减去1，所以最大不能超过剩下的数。从小到大遍历k，检测到一个符合条件的k就输出，没有的话就return -1。

#### [Snowflake Array Reduction](https://leetcode.com/discuss/interview-question/2550995/snowflake-OA), [Solution](List/Array_Reduction)
首先得到整个array的mex。然后找到第一个使得当前currMex等于mex的位置，同时在count里减去已经用过的元素。然后在更新过的count里找到nextMex，然后重复上一步。



---

<div id='Hashmap'></div>

## Hashmap

#### [1. Two Sum](https://leetcode.com/problems/two-sum/description/), [Solution](Hashmap/Two_Sum.py)
用hashmap储存与当前值的和为target的值，以及当前值的index。继续查找每一个值，如果在hashmap里就输出储存的index和当前的index。

#### [15. 3Sum](https://leetcode.com/problems/3sum/description/), [Solution](Hashmap/3Sum.py)
跟2sum基本一样，先排序，然后对每一个值把他当成2sum里的k，然后对之后的做2sum，依次重复n次。

#### [18. 4Sum](https://leetcode.com/problems/4sum/description/), [Solution](Hashmap/4Sum.py)
和3sum基本一样。另外这里面两个外部循环都有if i == 0 or nums[i - 1] != nums[i]，是用来避免重复计算的。

#### [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/description/), [Solution](Hashmap/Two_Sum_III_-_Data_structure_design.py)
跟Two Sum一样，不过把hashmap的值的index换成了count，因为只要找到是否有就行了不要下标。然后用count可以避免重复访问同一个元素。

#### [460. LFU Cache](https://leetcode.com/problems/lfu-cache/description/), [Solution](HashMap/LFU_Cache.py)
两个map。一个保存key, (frequency, value)对，一个保存frequency, keys对。key是OrderedDict。根据key查找frequency，更新两个map。同时维护当前有key的最小频率。

#### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/), [Solution](Hashmap/Subarray_Sum_Equals_K.py)
用一个hashmap记录到每个下标为止的子串合对应的子串数。对每个新下标，count加上合为 当前子串合 - k 的子串数。

#### [1282. Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/), [Solution](HashMap/Group_the_People_Given_the_Group_Size_They_Belong_To.py)
先过一遍group，找出每个size都有哪些人，然后对每个size里的那些人按size大小分组。

#### [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/), [Solution](HashMap/Minimum_Deletions_to_Make_Character_Frequencies_Unique.py)
用到了Counter和SortedSet。先过一遍Counter统计每个字母出现了多少次，然后过一遍Counter统计每个出现频率的字母有多少个。然后把出现频率放到sortedSet里，从大到小，把每个出现频率的字母减少字母个数减一个，然后如果出现频率大于一（说明可以减少该字母）且该出现频率对应的字母数也大于一（说明确实有字母被减少了），那就在该频率减一的频率上加上该频率对应的字母数减一（因为有一个字母没有被减少）。

#### [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/), [Solution](Hashmap/Max_Number_of_K-Sum_Pairs.py)
跟2sum基本一样。不过用count来记录，然后每碰到一个匹配的就count--，res++

#### [2488. Count Subarrays With Median K](https://leetcode.com/problems/count-subarrays-with-median-k/description/), [Solution](Hashmap/Count_Subarrays_With_Median_K.py)
得到k的下标，计算到k右边每个下标为止大于小于k的数的个数并保存在hashmap里；然后从k往左边一样计算，根据hashmap里的个数，加起来等于0或1的个数，就是从这个下标开始满足条件的subarray个数。

#### [2588. Count the Number of Beautiful Subarrays](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description/), [Solution](Hashmap/Count_the_Number_of_Beautiful_Subarrays.py)
要想到beautiful subarray就是subarray的依次xor等于0的意思。然后就是跟560一样了，用字典储存到每个位置的xor总和，然后每个新位置查一下字典里等于当前xor的个数，加到count上就行。这样从之前到当前位置的xor就为0了。

#### [2598. Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/), [Solution](Hashmap/Smallest_Missing_Non-negative_Integer_After_Operations.py)
按余数分类，同时记录当前余数个数。然后q从0开始，再r从0到value - 1，遍历余数集，直到余数集里找不到下一个，就是不存在的，然后返回q * value + r

#### [2661. First Completely Painted Row or Column](https://leetcode.com/problems/first-completely-painted-row-or-column/description/), [Solution](HashMap/First_Completely_Painted_Row_or_Column.py)
先过一遍，统计每个元素的行列。然后根据array，在每个位置对应的行列count+1。然后如果有达到填满某一行或者某一列的就返回这个位置的index。

#### [2671. Frequency Tracker](https://leetcode.com/problems/frequency-tracker/description/), [Solution](Hashmap/Frequency_Tracker.py)
两个hashmap，分别记录每个数的频率和每个频率对应的数。每次增减都更新这两个hashmap。

#### [2829. Determine the Minimum Sum of a k-avoiding Array](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/), [Solution](HashMap/Determine_the_Minimum_Sum_of_a_k-avoiding_Array.py)
简单，基本就是2sum。



---

<div id='LinkedList'></div>

## Linked List
#### [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/), [Solution](LinkedList/Add_Two_Numbers.py)
创建一个新链表，如果l1或l2后面还有就继续延长这个链表

#### [86. Partition List](https://leetcode.com/problems/partition-list/description/), [Solution](LinkedList/Partition_List.py)
把比x小的和大于等于x的元素分别放到两个list里然后再现重新生成一个linkedlist。

#### [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/), [Solution](LinkedList/Copy_List_with_Random_Pointer.py)
我用的简单的先复制再建立联系，可以用recursive的方法直接在复制的时候就建立联系。

#### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/), [Solution](LinkedList/Linked_List_Cycle.py)
遍历链表，把见过的放进set，之后如果碰到之前放进set过的就是cycle，否则不是。

#### [146. LRU Cache](https://leetcode.com/problems/lru-cache/description/), [Solution](LinkedList/LRU_Cache.py)
用双链表做。保存head和tail，然后自己写一个addNode和deleteNode函数。另外用一个dict保存key和对应node的指针。get的时候删掉对应node并再次加到头部；put的时候如果已经在里面就删掉，然后如果dict还是满的就说明put的是新元素，删掉tail前的node，然后再把新node的加到头部。

#### [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/description/), [Solution](LinkedList/Add_Two_Numbers_II.py)
过两遍linkedlist乘10相加，然后加起来再除10取余从尾到头建个新linkedlist。

#### [725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/description/), [Solution](LinkedList/Split_Linked_List_in_Parts.py)
根据剩余总数和剩余组数，如果能整除下一组就有正好整除那么多个node，不能的话就是整除向上取整那么多个。



---

<div id='Tree'></div>

## Tree


#### [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/description/), [Solution](Tree/Unique_Binary_Search_Trees_II.py)
写一个helper生成两个数之间的所有二叉树，然后以每个数为root，递归他的左右子树，然后组合起来以这个数为root的树。

#### [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Search_Tree.py)
跟下面一个基本一样，不过利用了BST的结构，直接判断当前节点的值，如果在p，q之间就是找到了，小于更小的或者大于更大的就去另一边找。

#### [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Tree.py)
用一个helper判断在当前子树中是否检测到p或q。在root，helper(root.left)，helper(root.right)中如果有两个检测到了就是找到了LCA，修改全局变量self.ans。每一层返回curr or 上面两个，这样就算找到了LCA，后续返回的也是True就是1，之后不会重复修改全局变量。

#### [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/description/), [Solution](Tree/Boundary_of_Binary_Tree.py)
直接分别取left boundary, leaves, and right boundary。

#### [894. All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/description/), [Solution](Tree/All_Possible_Full_Binary_Trees.py)
recursion做，对n个node的树递归左右子树从0到n - 1。同时用一个字典记录n个node的树的所有组合方式，之后递归到的时候就不用重复计算。

#### [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/), [Solution](Tree/Lowest_Common_Ancestor_of_Deepest_Leaves.py)
bfs找到deepest leaves，并记录每个node的parent。从最底层的leaves开始，回溯parent，直到只剩某一层一个parent。

#### [1676. Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/), [Solution](Tree/Lowest_Common_Ancestor_of_a_Binary_Tree_IV.py)
和基本情况差不多，不过这次不是检测是否只有两个，而是检测是否所有node都被在当前子树下找到了。

#### [2471. Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/), [Solution](Tree/Minimum_Number_of_Operations_to_Sort_a_Binary_Tree_by_Level.py)
用两个queue按层bfs遍历树，然后对每层求min swap。重点是min swap。注意iterative traversal的时候就用普通stack就行，然后先后顺序反过来。

#### [2673. Make Costs of Paths Equal in a Binary Tree](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description/), [Solution](Tree/Make_Costs_of_Paths_Equal_in_a_Binary_Tree.py)
在每个点让他的左右子路径相等。res加上左右子路径的差，然后更新这个点的cost到本来的cost加上子路径的cost。




---

<div id='Trie'></div>

## Trie
就是nested hashmap。一开始就是一个{}，每一层就加一个key，每到一个终点就在终点的hashmap里加一个'$'的key表示到达终点了。


#### [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/), [Solution](Trie/Design_Add_and_Search_Words_Data_Structure.py)
用Trie保存加进去的word，然后每次search检查。


#### [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/), [Solution](Trie/Word_Search_II.py)
先用一个trie记录所有word，然后从board的每个位置开始dfs。如果在trie里找到了，就去掉这个词。如果某个叶节点到底了而且已经找到过了，就去掉这个叶节点。


#### [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/description/), [Solution](Trie/Search_Suggestions_System.py)
用Trie记录product，并在每一层用suggestion记录三个词，然后对word每个字母到每一层的时候直接访问对应的suggestion。还可以用sort + binary search。



---


<div id='Graph'></div>

## Graph

#### [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/), [Solution](Graph/Find_Critical_and_Pseudo-Critical_Edges_in_Minimum_Spanning_Tree.py)
先排序，然后用Kruscal找出一个最小生成树并记录这个树的最小权。然后对每个边考虑不带这个边和强制带这个边，再用Kruscal看是否能组成等于最小权的最小生成树，来判断这个边是否是critical或seudo critical的。把union find写成一个类，方便后面每次Kruscal里方便调用。

#### [1615. Maximal Network Rank](https://leetcode.com/problems/maximal-network-rank/description/), [Solution](Graph/Maximal_Network_Rank.py)
简单，统计一下每个node的度然后暴力就行了。注意相连的node的network rank要减一。



---

<div id='Heap'></div>

## Heap

#### [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/), [Solution](Heap/Meeting_Rooms_II.py)
Use a heap to keep the end time of each room. Process meetings by their start time. If the start time is earlier than the earliest endtime, then it means more room is needed. Otherwise just allocate the already finished room to the current meeting.
#### [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/), [Solution](Heap/Find_Median_from_Data_Stream.py)
建一个最大堆和一个最小堆，保存他们的大小，每次有新的数进来就让他进最小或最大堆，保持最大堆和最小堆个数相等或者多1。

#### [767. Reorganize String](https://leetcode.com/problems/reorganize-string/description/), [Solution](Heap/Reorganize_String.py)
先算出每个字母的出现次数，然后依次把出现次数最多或第二多的append到末尾。用heap来看出现最多的字母。

#### [2386. Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/description/), [Solution](Heap/Find_the_K-Sum_of_an_Array.py)
先得到所有正数的和，这是可能得最大和。然后开始去掉和里的正数，或者加上剩下的负数，这两个都等价于从最大和里减去nums里的绝对值。因为是从最大和往下，所以把nums按绝对值排序之后依次减去每个值，并且每一步考虑加上nextSum - absNum[idx + 1]和nextSum + absNum[idx] - absNum[idx + 1]两种情况，即是否减去下标idx的值。每一步的结果都放到一个最大堆里，下一步再从最大堆里取，保证了是从maxSum依次往下递减。absNum排序过，也是用来保证maxSum依次递减。

#### [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/description/), [Solution](Heap/Meeting_Rooms_III.py)
用两个min heap，一个保存可以用的房间，一个保存使用中的房间，以结束时间为关健字。每一步先把结束时间小于当前开始时间的都挪到可用房间，如果当前有可用房间则直接用，没有的话则推迟当前meeting到下一个可以用的房间为止。

#### [2662. Minimum Cost of a Path With Special Roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/), [Solution](Heap/Minimum_Cost_of_a_Path_With_Special_Roads.py)
Dijrastra的想法，因为所有special road的终点从任何起点都是可达的，所以里面每一步都要更新到所有重点的距离。每次取出最小距离，然后更新先到这个点，然后走到其他road的起点，然后再走special road到相应终点的距离。最后res返回先到每一个终点，再正常走到target的距离，这些的最小距离。



---

<div id='Stack'></div>

## Stack

#### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/), [Solution](Stack/Valid_Parentheses.py)
stack记录正括号，对每个反括号用字典取正括号看是不是在stack末尾，且stack不空。最后检查stack是否空。

#### [71. Simplify Path](https://leetcode.com/problems/simplify-path/description/), [Solution](Stack/Simplify_Path.py)
按/分割，然后根据.和..决定pop还是不管还是加入stack，最后用/连接。

#### [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/), [Solution](Stack/Largest_Rectangle_in_Histogram.py)
可以用stack是因为实际只有n个rectangle要检查。每个height，和这个height往左往右到第一个比他矮的height为止，这个rectangle。假设已经有一个stack，里面放着从低到高排列的height，检测到新的height比stack末尾的height低的时候就开始依次pop。因为是从低到高，所以每pop一个就根据这个的height和他前一个的下标计算面积。到末尾再把剩下的全部pop出来。

#### [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/), [Solution](Stack/Maximal_Rectangle.py)
对每一行，保存到当前位置为止的连续1的个数。然后叠起来，从列来看，每一列就是一个histgram，就转化成了上一题84。所以预处理出n个hist之后，只用再对每一列做一次largest rectangle就可以了。

#### [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/description/), [Solution](Stack/Remove_Duplicate_Letters.py)
让stack里保存到当前位置为止的最小substring。如果当前元素不在里面就放进来。每次新元素进来，把前面stack里比这个大的且后面还有的pop出去。

#### [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/), [Solution](Stack/Next_Greater_Element_I.py)
首先预处理一个monostack，找到每个数的nextGreater。每步从末尾pop出stack里比当前元素小的元素的下标。用字典记录那个元素:当前元素。然后过nums1，在字典里找相应的元素。

#### [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/description/), [Solution](Stack/Next_Greater_Element_II.py)
过一遍monostack，每次pop出比当前小的元素的下标并更新那些元素的nextGreater。更新完之后把当前下标放进stack。再过第二遍，这样之前nextGreater在左边的也可以被更新了。

#### [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/description/), [Solution](Stack/Asteroid_Collision.py)
用stack记录asteroid， 每个新的如果往右那么不会和stack里已有的碰撞，直接加进去；如果往左就一直碰撞到自己消失或者没有可以碰撞的为止。

#### [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/), [Solution](Stack/Daily_Temperatures.py)
简单，每次pop出比当前低的temperature的下标就行。

#### [768. Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/), [Solution](Stack/Max_Chunks_To_Make_Sorted_II.py)
和769完全没区别啊。

#### [769. Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/description/), [Solution](Stack/Max_Chunks_To_Make_Sorted.py)
保存一个递增stack，里面每个数就是一个chunk的最大元素。每次把大于当前元素的都pop出来。当前元素前面比当前大的元素都必须和当前元素在同一个chunk里。

#### [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/), [Solution](Stack/Online_Stock_Span.py)
保存每个price和他前面小于等于他的price的个数。每次把stack末尾小于等于当前price的pop出来就行。

#### [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/), [Solution](Stack/Sum_of_Subarray_Minimums.py)
过两遍数组，找到每个元素右边第一个比他小的元素的下标，以及左边第一个小于等于他的元素的下标。在这两个之间，所有数组都以他为最小值。所以再过一遍数组，求这两个下标之间，包含这个元素的总数组数就行了。

#### [1996. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/), [Solution](Stack/The_Number_of_Weak_Characters_in_the_Game.py)
排序，atack从小到大，defence从大到小，然后从后往前遍历，保存目前见过的最大defence。因为atack从小到大，所以往前走的时候atack一直变小。因为defence从大到小，所以不会出现倒挂的情况。
还可以用greedy，就是先过一遍，找出对每个atack，比他大的那些atack里面，可能的最大defence。然后再过一遍，对每个atack，查找比他大的atack里面的最大defence是否比他自己的defence大。

#### [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/description/), [Solution](Stack/Buildings_With_an_Ocean_View.py)
维护一个decreasing stack。每次从stack末尾开始把高度小于等于当前高度的idx都pop掉。

#### [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/description/), [Solution](Stack/Sum_of_Subarray_Ranges.py)
和907基本一样，不过这次要对每个元素，同时找出以他为最大值的数组数和以他为最小值的数组数。每次这两个相减就行了。

#### [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/description/), [Solution](Stack/Removing_Stars_From_a_String.py)
直接一个stack往前走，碰到*就pop就行了。

#### [2645. Minimum Additions to Make Valid String](https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/), [Solution](Stack/Minimum_Additions_to_Make_Valid_String.py)
写的是dp，不过其实是stack，因为只有一维。对每个字符，根据他前面的字符分类讨论就行了。

#### [2696. Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/), [Solution](Stack/Minimum_String_Length_After_Removing_Substrings.py)
用stack，从头往后，监测到AB或者CD就pop。

#### [2751. Robot Collisions](https://leetcode.com/problems/robot-collisions/description/), [Solution](Stack/Robot_Collisions.py)
先排序，然后按照position顺序从左到右，用stack记录已有的robot，如果新加进来的是往左的就一直和stack末尾往右的robot碰撞，直到末尾不往右或者其中一个消失。一开始排序的时候记得把原来在position里的顺序也记录一下，最后按这个再排一次序，然后输出每个robot的health。



---

<div id='UnionFind'></div>

## Union Find
可以用来检查集合连通性。

#### [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/), [Solution](UnionFind/Most_Stones_Removed_with_Same_Row_or_Column.py)
对每个石头，连接他的row和col。因为row数有限，所以col直接+10001就行。最后检查有多少连通集。

#### [959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/description/), [Solution](UnionFind/Regions_Cut_By_Slashes.py)
把每个格子分成四个三角形，根据每一个位置是\或/或者空格，连接格子里的三角形。然后连接相邻格子的三角形。最后统计有多少三角形的root是他自己，即连同集个数。

#### [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/description/), [Solution](UnionFind/Number_of_Closed_Islands.py)
用unionfind做的，但里面废操作太多了。可以用bfs，每次开始bfs的时候设置一个boolean isclosed = True，之后如果碰到边界就改成False。这样依次bfs就可以了。

#### [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/), [Solution](UnionFind/Number_of_Operations_to_Make_Network_Connected.py)
找出不联通集的个数，返回个数减一。

#### [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/), [Solution](UnionFind/Remove_Max_Number_of_Edges_to_Keep_Graph_Fully_Traversable.py)
用union find来记录alice和bob的边是否都是连通的。最后检查加进去的边是不是等于n - 1。这里UF用的是一个列表，因为正好node都是从1到n标记的。用dict也可以，就是中间复制的时候要手动写一个deep copy。

#### [1627. Graph Connectivity With Threshold](https://leetcode.com/problems/graph-connectivity-with-threshold/description/), [Solution](UnionFind/Graph_Connectivity_With_Threshold.py)
先预处理，对threshold到n的每个数字用union find建立连通分量，然后每个query判断是否在一个等价类里面。

#### [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/), [Solution](UnionFind/Checking_Existence_of_Edge_Length_Limited_Paths.py)
先对queries和edges分别排序，然后对每个query，把distance小于当前query的limit的那些edge用union连起来，然后用find判断当前query的p和q是否连同。因为只连接了小于当前limit的所有边，所以直接判断就行，不用另外看每个边的distance。

#### [2493. Divide Nodes Into the Maximum Number of Groups](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/), [Solution](UnionFind/Divide_Nodes_Into_the_Maximum_Number_of_Groups.py)
对每一个node做bfs就可以得到最大group数。用union find来记录连通分量。其实不用union find也可以，只要记录了连通分量就可以。

#### [2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/description/), [Solution](UnionFind/Count_the_Number_of_Complete_Components.py)
先找到连通集，然后看每个连通集是否是complete的。


---

<div id='Math'></div>

## Math

#### [50. Pow(x, n)](https://leetcode.com/problems/pow(x,-n)/description/), [Solution](Math/Pow(x,_n).py)
暴力会超时，所以根据n的二进制表示来考虑结果里有哪些x的二次power。可以用bitmask或者recursion。从小到大可能会超出float范围，所以可以限制将超出范围的时候返回0（因为答案不会超出范围，中间的power超出范围就说明是负幂就是除）。也可以从大到小做，不会超出范围。

#### [1359. Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/), [Solution](Math/Count_All_Valid_Pickup_and_Delivery_Options.py)
就是插空，每多一对就在之前的所有里面的空隙之间插入。

#### [2850. Minimum Moves to Spread Stones Over Grid](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/), [Solution](Math/Minimum_Moves_to_Spread_Stones_Over_Grid.py)
首先看哪些位置大于1，哪些位置等于0，然后放进list。大于1的放进去x - 1次，x是具体数值，表示这个位置要被分配x - 1次。然后计算这两个list里面每两个点之间的曼哈顿距离，这里用了scipy.spatial.distance.cdist这个函数。然后就是一个找矩阵最小分配cost问题，用的算法是[Hungatian](https://en.wikipedia.org/wiki/Hungarian_algorithm)算法。直接用了scipy.optimize.linear_sum_assignment这个函数。



---

<div id='Prime'></div>

## Prime

- 筛法
- all primes are either 2， 3， 或者6n - 1/6n + 1 for some n
范围不大可以用筛法，这样筛一次就行了。但是空间需求很大。如果数字范围很大就用prune，只有用到了才会算空间。

#### [2523. Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range/description/), [Solution](Prime/Closest_Prime_Numbers_in_Range.py)
主要注意怎么筛素数。对小于x的素数，从2到sqrt(x)为止，如果i是素数就把i的所有倍数都标位合数，依次标记。最后把没被标记为合数的拿出来，就剩下的是素数。

#### [2572. Count the Number of Square-Free Subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/description/), [Solution](Prime/Count_the_Number_of_Square-Free_Subsets.py)
其实算是dp了。注意空集的时候返回的是1，因为要和其他情况组合，其他子集里可能有元素，所以不返回0。最后再只减去一个1，就是所有子集都为空集的情况。

#### [2614. Prime In Diagonal](https://leetcode.com/problems/prime-in-diagonal/description/), [Solution](Prime/Prime_In_Diagonal.py)
用prune，然后对每个对角线上的元素，用sqrt之后再prune了的子集来判断是否是素数。用到了lambda函数，filter，all，集合的并｜，sorted。




---

<div id='Sort'></div>

## Sort

#### [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2/problem), [Solution](Sort/Minimum_Swaps_2.py)
把数组看成一个图，每个数字是一个节点，从当前位置到排序好后应该在的位置有一条边，得到一些不交的圈。最后swap数 = sum(每个圈的大小 - 1)。按顺序遍历排序后的数组，用元组保存原始位置，通过访问原始位置来遍历整个圈。用一个list或者set来track是否每个元素都visit了。

#### [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/), [Solution](Sort/Kth_Largest_Element_in_an_Array.py)
最简单的是用heap。然后可以用快速选择，每一步选一个pivot然后partition，返回partition后的pivot下标。如果下标等于k smallest就返回，否则根据相对大小在pivot左边或者右边继续找。可以iterative来做，就是给一个start一个end，每一步把start或end重新定位到partition之后的pivot，直到start等于end。

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

<div id='PrefixSum'></div>

## Prefix Sum


#### [370. Range Addition](https://leetcode.com/problems/range-addition/description/), [Solution](PrefixSum/Range_Addition.py)
先用cache记录每个query开始的位置和结束的下一个位置，然后过一遍，期间每个位置的currSum加上对应的cache。

#### [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/description/), [Solution](PrefixSum/Corporate_Flight_Bookings.py)
同370。一模一样只能说。


#### [1094. Car Pooling](https://leetcode.com/problems/car-pooling/description/), [Solution](PrefixSum/Car_Pooling.py)
同370，不过这次用的是dict来当cache。上面一个其实也可以，不过因为上面本来就要返回一个list所以直接用了list。

#### [2281. Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/description/), [Solution](PrefixSum/Sum_of_Total_Strength_of_Wizards.py)
先算出每个元素右边第一个比他小的下标，左边第一个小于等于他的下标，然后对每个元素，计算所有以他为最小元素的数组的和。这里要用两次prefix sum，并且最后算的时候数组和是这样 racc * ln - lacc * rn 的形式。自己想大概是想不出来的，只能看碰到的话记不记得了。

#### [2536. Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/description/), [Solution](PrefixSum/Increment_Submatrices_by_One.py)
对每一行做一次prefix sum。另外也可以用2dcache来做，在每个矩形的左上角、右下角外+1，右上角外、左下角外-1不过还没看懂，之后有兴趣可以看看[这里](https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-with-visualization-clean-concise/)。

#### [2615. Sum of Distances](https://leetcode.com/problems/sum-of-distances/description/), [Solution](PrefixSum/Sum_of_Distances.py)
用dict存数和对应的下标。距离里面把每个绝对值号拆开，然后就可以有公式了。对每个数，先算一个prefix sum，然后每个下标里面套公式和prefix sum就行了。

#### [2670. Find the Distinct Difference Array](https://leetcode.com/problems/find-the-distinct-difference-array/description/), [Solution](PrefixSum/Find_the_Distinct_Difference_Array.py)
先过一遍，保存prefix和sufix sum，然后直接算结果。



---

<div id='BinarySearch'></div>

## Binary Search

#### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/), [Solution](BinarySearch/Search_in_Rotated_Sorted_Array.py)
先通过left和mid的大小关系判断转折点在左边还是右边，然后再通过target和递增那一边的两端的大小关系判断target在哪边。

#### [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/), [Solution](BinarySearch/Search_a_2D_Matrix.py)
bisect_left返回下标i，这之前的所有元素严格小于搜索的元素x，i及i之后的元素大于等于x。先搜索所有行的第一个元素。如果返回的下标元素等于target则结束。否则说明target在下标对应的那一行（可能超出）。然后在下标对应的行再次搜索，判断搜索出来的元素是否等于target。

#### [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/), [Solution](BinarySearch/Search_in_Rotated_Sorted_Array_II.py)
和33基本一样，加一个步骤每轮如果left和right和相邻的相等就往中间移动，这样保证nums[left] <= nums[mid]的时候转折点肯定在右边，否则在左边的话说明mid到right为止全都相等，那right就会一直往左走直到不相等。

#### [704. Binary Search](https://leetcode.com/problems/binary-search/description/), [Solution](BinarySearch/Binary_Search.py)
简单。可以把相等情况放在第一个判断，这样可以不用每次都运行到最底端，而且可以避免中间out of range。

#### [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/), [Solution](BinarySearch/Peak_Index_in_a_Mountain_Array.py)
每次判断mid和他左右元素的大小，如果不是mid - 1 < mid > mid + 1就说明不是peak，根据落在peak左边或右边决定下一步binary的方向。

#### [1870. Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/), [Solution](BinarySearch/Minimum_Speed_to_Arrive_on_Time.py)
从最小速度到最大速度之间二分搜索。另外用一个函数来验证每个速度是否能达到。

#### [2300. Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/), [Solution](BinarySearch/Successful_Pairs_of_Spells_and_Potions.py)
对potions排序，然后在里面找对应每个success/spell的下标，有了下标就可以直接得到个数了。

#### [2439. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array/description/), [Solution](BinarySearch/Minimize_Maximum_of_Array.py)
就是snowflake的oa。不过有O(n)解法，greedy，明天再看看。

#### [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/), [Solution](BinarySearch/Minimum_Cost_to_Make_Array_Equal.py)
cost函数是凸函数，所以可以用二分法来找这个最小值。每一步计算mid和mid + 1的cost，判断最小值点在mid的左边还是右边，然后二分就行了

#### [2517. Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/), [Solution](BinarySearch/Maximum_Tastiness_of_Candy_Basket.py)
感觉binary sort这种的越来越多了。对tastiness二分，每步检查是否有一组k个candy，tastiness大于等于mid。

#### [2610. Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/), [Solution](Hashmap/Convert_an_Array_Into_a_2D_Array_With_Conditions.py)
counter看一下每个数出现次数，然后依次往里面放就行了。

#### [2616. Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/), [Solution](BinarySearch/Minimize_the_Maximum_Difference_of_Pairs.py)
mini max问题用二分法。这里每次检测mid这个最大difference可不可以达到。因为排序后的所有最小difference肯定出现在相邻元素之间，所以每次检测的时候只用检测那些相邻的元素就行了。

#### [2718. Sum of Matrix After Queries](https://leetcode.com/problems/sum-of-matrix-after-queries/description/), [Solution](BinarySearch/Sum_of_Matrix_After_Queries.py)
先想到用list来储存每一列每一行最后更新的数和更新顺序，然后每一列二分找这一列里在当前列顺序之前更新的行数，然后这些行被列覆盖，剩下的保持行的数。

#### [2817. Minimum Absolute Difference Between Elements With Constraint](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/), [Solution](BinarySearch/Minimum_Absolute_Difference_Between_Elements_With_Constraint.py)
从第x位开始，每一步把他之前的第x个元素放到sortedlist里。这样可以保证轮到每个元素的时候，他x位之前的数都在sortedlist里。然后每一步再sortedlist里二分找离当前元素最近的元素。因为加元素的方式，保证了里面所有元素都离当前元素至少x位。然后比较二分出来的位置上的元素和当前元素的差，并更新当前的最小差。这里用了sortedcontainers，而且sortedcontainers里的结构可以直接call bisect_left函数。

#### [Snowflake Perfect Pairs](https://leetcode.com/discuss/interview-question/1781247/TuSimple-or-OA-or-Perfect-Pairs)
条件2总是满足的，而条件1等价于|x| <= |y|, |y| <= 2|x|。所以先取绝对值，排序，然后从前往后对每个下标i，找到i < j, nums[j] <= 2nums[i]的最大的j。从i + 1到j都是满足和i的perfect pair。

#### [Snowflake Cross the Threshold](https://www.1point3acres.com/bbs/thread-931627-1-1.html)
可以用二分查找答案范围，也可以先排序然后递增barrier来逐步减小sum。都是nlogn。

#### [Snowflake Maximize Array Value](https://leetcode.com/discuss/interview-question/2140142/Snowflake-OA-or-Maximize-Array-Value), [Solution](https://maplezoo.notion.site/Maximize-Array-Value-4c8551f092e94daf8b7aca3228e9c81a), [Solution](BinarySearch/Maximize_Array_Value.java)
从0到最大值二分查找。每轮验证当前的max是否可以达到。i从后往前，diff = Math.max(nums[i] + diff - max, 0);这里如果nums[i] <= max就没问题，否则作为diff传到下一个数，这个diff需要在之后被抹平。如果到0都没被抹平就说明当前的max无法达到；diff最后为0则说明可以达到。

#### [Snowflake Largest Sub-grid](https://leetcode.com/discuss/interview-question/1215695/Microsoft-OA-Largest-Sub-grid), [Solution](https://maplezoo.notion.site/Largest-subgrid-c0b3d259c7d84bd58a93866497b2a3db)
在最小max，1x1，和最大max，nxn里面二分，求满足条件的最大kxk。

#### [Snowflake Server Selection](https://leetcode.com/discuss/interview-question/2594968/Snowflake-or-OA-or-Server-Selection), [Solution](https://leetcode.com/discuss/interview-question/2594968/Snowflake-or-OA-or-Server-Selection)
对答案二分。二分的每一步中假设现在是x，首先过一遍vulnerability，把大于等于x的元素标位1，其他是0。然后再过一遍，记录每一行1的个数。这个和前面可以合成一步。再对每一列，记录第一个为1的行的index。如果有一列找不到说明不管怎么取这一列的min都小于x，往左二分。都找到之后如果行index的数量小于M说明可以，向右二分，包含当前x。如果index数等于M但是其中存在一行，1的count数大于1，说明有一行可以覆盖多列，一样可以，向右二分。否则向左二分。


---

<div id='SlidingWindow'></div>

## Sliding Window

#### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/), [Solution](SlidingWindow/Longest_Substring_Without_Repeating_Characters.py)
记录之前每一个数的下标，以及left。每一步如果以前记录过且在window内，则更新left到记录过的下标+1，否则不用管。然后把当前元素的下标也记录进去。最后更新res到当前下标 - left + 1.

#### [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/), [Solution](SlidingWindow/Sliding_Window_Maximum.py)
要想到maintain一个deque，储存当前window里从最大元素开始往右依次减小的下标。这样第一个下标始终是当前window里最大元素的下标。因为加进去一个数之后window里面这个数之前的元素就都没用了，所以window是单调的。用一个clean函数来维护，clean是O(1)的。首先从左边去掉不在window里的下标，然后从右边开始去掉小于当前元素的下标。因为维护前是从大到小，所以维护后也是从大到小。然后用这个deque遍历nums就行了。

#### [1100. Find K-Length Substrings With No Repeated Characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/), [Solution](SlidingWindow/Find_K-Length_Substrings_With_No_Repeated_Characters.py)
用一个set储存当前window里的元素方便快速查找，用一个deque按顺序储存当前window的元素和下标。每一步，如果window已经满了，丢掉最前面的，更新window大小；如果新元素已经在window里，丢掉到重复元素位置并根据最后丢掉的元素的下标更新window大小；最后把新的元素放进来，如果window是满的就substring数加一。

#### [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/description/), [Solution](SlidingWindow/Jump_Game_VI.py)
和239一样，用一个mono deque记录每个下标位置的最大score，每一步更新并保持window单调下降，且window里score最大的在第一个。

#### [1852. Distinct Numbers in Each Subarray](https://leetcode.com/problems/distinct-numbers-in-each-subarray/description/), [Solution](SlidingWindow/Distinct_Numbers_in_Each_Subarray.py)
滑动窗口，用字典统计窗口的的数字和个数。

#### [2516. Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/), [Solution](SlidingWindow/Take_K_of_Each_Character_From_Left_and_Right.py)
直接sliding window就行了。。。每加进来一个就检测窗口内元素是否过多，过多就一直++左边界，不然就重复加新元素。  

#### [2537. Count the Number of Good Subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/description/), [Solution](SlidingWindow/Count_the_Number_of_Good_Subarrays.py)
用hashmap记录当前window里的good pair。然后right右移hashmap对应增加，left左移直到window里count数小于k。

#### [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/), [Solution](SlidingWindow/Count_Complete_Subarrays_in_an_Array.py)
统计以每个下标作为左边界的所有complete subarray。窗口往右滑，如果当前窗口是一个complete subarray那么从当前窗口往右的所有subarray都是complete的。然后窗口左边右移一位，如果当前窗口不complete了就右移右边界直到complete，如果直接complete就直接统计。

#### [2831. Find the Longest Equal Subarray](https://leetcode.com/problems/find-the-longest-equal-subarray/description/), [Solution](SlidingWindow/Find_the_Longest_Equal_Subarray.py)
先预处理，得到每个数以及包含这个数的所有区间，然后对每个数的区间用sliding window，依次加入下一个区间直到count超过k，然后就把window头部的区间pop出去。


---

<div id='TwoPointer'></div>

## Two Pointer

#### [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/), [Solution](TwoPointer/Sort_Colors.py)
可以直接用quicksort，merge sort之类的。还有一个O(N)的方法，保持三个指针，p0, p2, curr。p0左边全是0，p2右边全是2，curr是当前位置。如果当前是0，交换curr和p0。因为curr在p0右边，所以从p0换过来的是已经检测过的，p0和curr都可以++。如果curr是1则不变。如果curr是2，交换curr和p2，p2--。这里因为从p2交换过来的没有检测过，所以curr不能前移，要保持在原地。

#### [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/), [Solution](TwoPointer/Two_Sum_II_-_Input_Array_Is_Sorted.py)
Two Sum可以用two pointer做也可以用hashmap做，用two pointer的缺点是要先排序，优点是空间O(1)。这里既然已经排过序了，就可以直接用two pointer。

#### [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/), [Solution](TwoPointer/Two_Sum_IV_-_Input_is_a_BST.py)
BST的inorder遍历会得到一个nondecreasing的序列。所以用一个inorder+twopointer就行了。

#### [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/description/), [Solution](TwoPointer/Boats_to_Save_People.py)
排序之后依次匹配最小的和最大的，小于等于limit就一起放进去，否则只把大的放进去。

#### [1099. Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/description/), [Solution](TwoPointer/Two_Sum_Less_Than_K.py)
先排序，然后用two pointer。很简单。还可以利用题目的条件k在1-1000之间，不过这个感觉不够通用，就算了。

#### [1372. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/), [Solution](DFS/Longest_ZigZag_Path_in_a_Binary_Tree.py)
从root开始DFS，可以用一个self全局变量记录。另外其实可以不用memo，因为每条路只计算了一次。

#### [2576. Find the Maximum Number of Marked Indices](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/), [Solution](TwoPointer/Find_the_Maximum_Number_of_Marked_Indices.py)
先排序。因为最多有n//2对，所以j从(n + 1) // 2开始。之后i从0开始，满足条件就i++，否则不变。最后i * 2就行。

#### [2597. The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/description/), [Solution](DP/The_Number_of_Beautiful_Subsets.py)
按除k的余数分类，然后在每个子集里讨论。每个子集里如果和前一个恰好差k就不能取，就是house robber问题。中间每一步乘的是v - 1，因为考虑的是取当前元素的情况，所以减去全部不取的那个情况。同样，最后返回res - 1也是这样。


---

<div id='DFS'></div>

## DFS

#### [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/), [Solution](DFS/Letter_Combinations_of_a_Phone_Number.py)
简单，recursive遍历，对前一步生成的所有组合加上这一步的数字对应的所有字母。

#### [77. Combinations](https://leetcode.com/problems/combinations/description/), [Solution](DFS/Combinations.py)
简单。下一个长度的combination由上一个长度加上所有可能得没用到的数组成。也可以用recursion。

#### [79. Word Search](https://leetcode.com/problems/word-search/description/), [Solution](DFS/Word_Search.py)
从board的每个位置开始dfs+backtrack搜索word。注意先pre check是否board里包含了word里的所有字母，不然会超时。

#### [133. Clone Graph](https://leetcode.com/problems/clone-graph/description/), [Solution](DFS/Clone_Graph.py)
保存一个seen dict，然后对每个neighbor迭代clone。

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

#### [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/description/), [Solution](DFS/Predict_the_Winner.py)
maxDiff记录从这个player开始，他能达到的最大difference。A可以从左边或右边拿，A拿了之后B拿，B依然要从B开始最大化他的difference。那么A的difference就是A拿左边或右边之后减去B的maxDiff，两个里面更大的那一个。

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

#### [2538. Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description/), [Solution](DFS/Difference_Between_Maximum_and_Minimum_Price_Sum.py)
用两次dfs，第一次以0为root，算出每个节点的最大和；第二次从0开始，往下dfs的时候传一个parent_contribution，即在每个节点的parent方向的最大路径和。为了计算parent_contribution，在每个节点算出包含他自己的parent_contribution在内的前两大的路径和。这样在所有子节点上，如果碰到了最大路径的节点，就把第二大的作为parent_contribution传入。

#### [2811. Check if it is Possible to Split Array](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/description/), [Solution](DP/Check_if_it_is_Possible_to_Split_Array.py)
dp，对每个子列[i:j]检查[i:j - 1]或[i + 1:j]是否满足当前条件且本身可以被split。



---

<div id='BFS'></div>

## BFS


#### [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/), [Solution](BFS/Binary_Tree_Level_Order_Traversal.py)
简单，用两个q交替记录当前层和下一层的node，然后每层的val依次append到一个list里。

#### [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/description/), [Solution](BFS/Word_Ladder_II.py)
首先建一个interword的字典，保存这些interword可以通向哪些word。然后从begin word开始bfs。TLE了。

#### [127. Word Ladder](https://leetcode.com/problems/word-ladder/description/), [Solution](BFS/Word_Ladder.py)
因为只要找到endWord就行，所以可以直接bfs+visited，不管中间是否有路径重叠。注意用一个interWord保存中间态，预处理wordList找到所有中间态，然后每一步转换成中间态之后再查找这个中间态可以到达哪些词。

#### [317. Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/description/), [Solution](BFS/Shortest_Distance_from_All_Buildings.py)
可以从每个空地开始bfs到每个building，或者从building开始bfs到空地。从building开始还可以每一步只bfs之前能bfs到的那些空格，可以更快。从空地开始的会超市。

#### [542. 01 Matrix](https://leetcode.com/problems/01-matrix/description/), [Solution](BFS/01_Matrix.py)
先把所有0的距离置为0，然后从0开始出发bfs，把剩下的所有距离安上。

#### [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/), [Solution](BFS/Maximum_Width_of_Binary_Tree.py)
bfs，每一层计算每个点的index，这一层过完之后更新最大index差，即宽度。

#### [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/description/), [Solution](BFS/Number_of_Enclaves.py)
和昨天的一样，不过可以从边界开始bfs，然后统计没有被bfs到的1的个数。

#### [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/), [Solution](BFS/Reorder_Routes_to_Make_All_Paths_Lead_to_the_City_Zero.py)
简单bfs。先记录所有单向边并同时保存双向边。然后从0出发bfs延双向边走，每走一步判断当前对应的单向边是否指向0，不指向的话就count + 1。

#### [2577. Minimum Time to Visit a Cell In a Grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/), [Solution](BFS/Minimum_Time_to_Visit_a_Cell_In_a_Grid.py)
bfs + heap。依次把没去过的点放到heap里面，注意四周的点的到达时间取max(time + 1, grid[nrow][ncol] + wait)。



---

<div id='DP'></div>

## DP

#### [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/description/), [Solution](DP/Unique_Paths_II.py)
简单dp，根据当前位置是否有障碍物决定返回上方和左方的和或是直接0.

#### [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/), [Solution](DP/Unique_Paths.py)
简单dp。

#### [72. Edit Distance](https://leetcode.com/problems/edit-distance/), [Solution](DP/Edit_Distance.py)
明明是DP不是DFS啊。如果作change，看看当前位置的character是否一样。如果作delete，在dp[i-1][j]上加1。如果作insert，在dp[i][j-1]上加1。取三个里面最小的。

#### [87. Scramble String](https://leetcode.com/problems/scramble-string/description/), [Solution](DP/Scramble_String.py)
可以用recursion，很简单，不过要加cache。也可以手动加。另外也可以三维bottom to top dp，dp[length][i][j]表示从s1第i位开始，s2第j位开始，长为length的子串是否scramble。

#### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/description/), [Solution](DP/Interleaving_String.py)
用的算是brute force+cache，但其实可以用DP。dp[i][j]储存能否用s1[:i+1]和s2[:j+1]interleave出s3[:i+j+1]。

#### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock.py)
简单，甚至不能称为dp，保存到目前为止的最小值，取当前价格和当前最小值的差并更新当前最大值。

#### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_II.py)
因为可以卖无限次，所以只要后一天比前一天价格高就可以买进卖出。

#### [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_III.py)
dp[k][i]是最多进行k次交易，最后一次最多在prices[i]卖出，的最高总收益。所以如果最后一次不在prices[i]卖出，就等于dp[k][i - 1]；如果卖出，就等于prices[i] - prices[j] + dp[k][j - 1] for j = 0, ..., i。因为只有j在变，所以等价于求min of prices[j] - dp[k][j - 1]。因为这里只有j在变，所以直接用min(currMin, prices[i] - dp[k][i - 1])就行了，因为比i小的已经在前面算过了，这里只要算当前值会不会更小就行。

#### [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_IV.py)
和123一模一样，就是推广到最多进行k次交易。另外注意这里允许在同一天先买进再卖出。

#### [198. House Robber](https://leetcode.com/problems/house-robber/description/), [Solution](DP/House_Robber.py)
最简单的一维dp。

#### [213. House Robber II](https://leetcode.com/problems/house-robber-ii/description/), [Solution](DP/House_Robber_II.py)
用原版house robber作辅助函数，根据拿不拿nums[-1]分两种情况，分别做两次dp。

#### [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/), [Solution](DP/Longest_Increasing_Subsequence.py)
dp[i] = 以第i个元素结尾的最长递增子序列。di[i] = max(dp[j] + 1) if dp[i] > dp[j] for j < i.

#### [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/), [Solution](DP/Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py)
建一个两行的dp，第一行表示在当前位置没有卖出，第二行表示在当前位置卖出了。迭代思路和k次交易的一样，用一个currMin来减少运算。最后取两行末尾的最大值。

#### [322. Coin Change](https://leetcode.com/problems/coin-change/description/), [Solution](DP/Coin_Change.py)
很标准的dp题，对用到的硬币数量和amount大小进行dp。

#### [337. House Robber III](https://leetcode.com/problems/house-robber-iii/description/), [Solution](DP/House_Robber_III.py)
recursion + memorization。根据拿不拿root分类。加上点边界条件就行了。

#### [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/),[Solution](DP/Combination_Sum_IV.py)
对target进行dp，以nums里的每个数num作结尾都是不同的组合，然后dp(target-num)。用cache加记忆。

#### [403. Frog Jump](https://leetcode.com/problems/frog-jump/description/), [Solution](DP/Frog_Jump.py)
不是最优解，差不多是brute force+cache。可以用DP。用一个字典储存key:value, key是每个位置，value是能到这个位置的jump的长度的集合。最后如果最后一个位置在字典里，就说明可以跳到这里，否则不可以。

#### [494. Target Sum](https://leetcode.com/problems/target-sum/description/), [Solution](DP/Target_Sum.py)
用的recursive dp，加一个字典memorization。还可以优化从传数组变成传下标。

#### [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/), [Solution](DP/Longest_Palindromic_Subsequence.py)
dp，每次比较i，j和i + 1， j - 1加上头尾是否相等、i + 1， j、i， j - 1之间的最大值。

#### [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/), [Solution](DP/Coin_Change_II.py)
每个coin有两种可能，用到或者不用到。所以对coin的index和amount做dp，每次考虑用到或者不用到这个coin的情况。

#### [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/), [Solution](DP/Course_Schedule_III.py)
先按结束时间排序，然后依次处理。维护到当前位置的上的最多的课，每个课的时长，和总时长。新的课来了之后，如果在当前时间直接上不超过lastDay，就直接放进heap里；如果超过了，duration大于之前的所有课的最大时长的话，不能放，否则无法维护是上的最多的课；如果小于之前的最大时长，则直接替换，可以维护是上的最多的课。因为是按结束时间排序，所以可以直接放进去替换。因为用了heap，所以总时长和之前上的课的时长也可以快速维护。

#### [664. Strange Printer](https://leetcode.com/problems/strange-printer/description/), [Solution](DP/Strange_Printer.py)
dp[i][j]表示从s第i个到第j个的substring的最少print数。每有一个新的进来，如果和前一个一样dp就也一样。如果不一样那就有两种方法。一个直接在dp[i][j - 1]基础上多print一次，一个从前一个相同字符开始覆盖到这里，然后重新print中间的部分。每一步对前面的所有元素都判断一次。

#### [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/), [Solution](DP/Number_of_Longest_Increasing_Subsequence.py)
简单dp，不过edge case弄了一会。用dp记录数组(l, s)，l是以当前元素为结尾的最长递增序列的长度，s是以当前元素为结尾的最长递增序列数。每个新元素过一遍前面的所有元素，如果前面的比当前的小那就是递增序列，根据前面的长度决定是否是最长递增序列以及是否加到现在的计数里去。

#### [688. Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/description/), [Solution](DP/Knight_Probability_in_Chessboard.py)
用棋盘记录每一步在每个格子上的概率。每一步更新整个棋盘所有格子的概率。最后对最后一步之后的整个棋盘上的概率求和。

#### [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/description/), [Solution](DP/Cherry_Pickup.py)
第二次不用从n-1, n-1往回走了，直接从0, 0往右下出发两个路径，然后三维dp，dp[r1][c1][r2]，然后让两个点在同一反对角线上，这样c2 = r1 + c1 - r2。

#### [808. Soup Servings](https://leetcode.com/problems/soup-servings/description/), [Solution](DP/Soup_Servings.py)
dp用一个helper function分别返回A先empty的概率和同时empty的概率。注意n过大时因为serve的方式不对称所以A先empty的概率接近1。所以n过大时直接返回1就行了。

#### [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/description/), [Solution](DP/Minimum_Cost_For_Tickets.py)
基本dp，根据在第i天用1/7/30pass来分类，取里面的最小的。另外注意bisect.bisect_left和bisect.bisect，第一个是使找a[:i] < x，a[i:] >= x的下标i，第二个是a[:i] <= x，a[i:] > x的下标i。

#### [1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/description/), [Solution](DP/Valid_Palindrome_III.py)
直接dp，能不能变成palindrome取决于变成palindrome的最小次数是否小于k。dfs(i, j)如果s的i和j相等，则等于dfs(i+1, j-1)。否则说明i或者j之间要去掉一个，就等于1+min(dfs(i+1, j), dfs(i, j-1))。

#### [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/), [Solution](DP/Maximum_Profit_in_Job_Scheduling.py)
直接dp，用recursion+lru_cache可以直接过，用memorization的话就必须用二分搜索。dp(i) = dp(i+1)或者对第i个工作结束时间之后的所有工作j，profit[i]+dp(j)中最大的那个。

#### [1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/), [Solution](DP/Minimum_Number_of_Taps_to_Open_to_Water_a_Garden.py)
dp[i]表示从0到i需要的最少tap数。然后遍历每个tap考虑用到这个tap的情况下，用这个tap覆盖范围内的dp[j]来更新这个tap的最远覆盖点处的dp。就是每个dp[j] + 1里面最小的那个。

#### [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/), [Solution](DP/Minimum_Difficulty_of_a_Job_Schedule.py)
直接dp，dp(i, d)表示从第i个工作开始，还剩下d天。dp(i, d)等于在当天安排从i到j-1的工作，然后剩下的d-1天做j之后的工作，即dp(j, d-1)，对所有j > i里面最小的那一个。用lru_cache减少时间。

#### [1444. Number of Ways of Cutting a Pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/), [Solution](DP/Number_of_Ways_of_Cutting_a_Pizza.py)
3d的DP。能想到3d的话就还好。看起来dp还是专门留一行空的出来比较好，这样就不用初始化了。

#### [1639. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/), [Solution](DP/Number_of_Ways_to_Form_a_Target_String_Given_a_Dictionary.py)
先找出每个下标上每个字母出现的次数，然后dp。dp(t, n)对应用word[:n]拼出target[:t]的方法数。

#### [2222. Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/description/), [Solution](DP/Number_of_Ways_to_Select_Buildings.py)
dp[k][j]为在s[:i + 1]中选择长度为k的挑选方法数。同时分别保存其中以'0'和'1'结尾的方法数。dp[k + 1[j]考虑是否以s[j]结尾，不结尾直接用前一个，结尾再加上dp[k][j - 1]里面结尾元素和s[j]不同的方法数。

#### [2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/description/), [Solution](DP/Substring_With_Largest_Variance.py)
用dp，相当于max subarray的一个变体。分别判断所有两个字母的组合，最多25x26种组合，每个组合花O(n)的时间。判断当前字母并增减max_subarray后，根据后续是否无任何字母或两个字母都有还是其他，判断是中断本次循环还是重置窗口还是继续当前循环。

#### [2291. Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks/description/), [Solution](DP/Maximum_Profit_From_Trading_Stocks.py)
一个budges * n的dp。有一些edge case，像初始化，在有足够钱且当前收益为正的情况下才进行交易等。

#### [2305. Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/description/), [Solution](DP/Fair_Distribution_of_Cookies.py)
DP+bitmask。几个操作1 << n是bit往左移n位。a & b，a ^ b。用整数表示一个组合，他的bit表示1的位置说明取到这个位置的元素。对mask求和里面mask & (1 << i)表示mask里第i个位置是否为1.然后从bagMask开始往下取mask = (mask - 1) & bagMask。因为&操作只会把数变小，所以是从大往小取。每轮里面取res = min(res, max(sum1, sum2))，因为是要取最小的最大值。sum1 = sumMask(mask)是这个mask单独分给一个人的和，sum2 = unfairness(k - 1, bagMask ^ mask)是bagMask去掉mask后剩下的cookie分给其他人的最大值。

#### [2444 Count Subarrays With Fixed Bounds](https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/), [Solution](DP/Count_Subarrays_With_Fixed_Bounds.py)
先过一遍nums，记录每个坐标前最近的等于minK，等于maxK，超出范围的值的坐标，记为prev[0], prev[1], prev[2]。然后dp。dp[i] = dp[i-1]，如果nums[i]没超出范围，那么dp[i]再加上prev[0], prev[1]里更小的那个到prev[2]的距离。如果是负的就不加。

#### [2369. Check if There is a Valid Partition For The Array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/), [Solution](DP/Check_if_There_is_a_Valid_Partition_For_The_Array.py)
基础dp，dp[i]取决于i之前的两个或三个数字是否满足条件以及更之前的dp是否valid。

#### [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/), [Solution](DP/Maximum_Number_of_Non-overlapping_Palindrome_Substrings.py)
dp检查到i下标之前的子串，里面长度大于k的回文串的最大长度。注意这里对以i-1结尾的子串，只用检查长度为k和长度k-1的就行，更前面的不用检查。

#### [2518. Number of Great Partitions](https://leetcode.com/problems/number-of-great-partitions/description/), [Solution](DP/Number_of_Great_Partitions.py)
dp[i][j]表示在nums[:i]中和为j的子集数。j从0到k - 1，dp[-1][j]就是nums中和为0到k - 1的所有子集数。在所有2^n种组合中减去第一组的和及第二组的和小于k的子集数。关键要能想到这么算。

#### [2547. Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/description/), [Solution](DP/Minimum_Cost_to_Split_an_Array.py)
切木条的变种，区别是切木条里面相应长度木条的价格都给出来了，这里要先算一下每个nums[i:j]的cost并记录。

#### [2684. Maximum Number of Moves in a Grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/), [Solution](DP/Maximum_Number_of_Moves_in_a_Grid.py)
基本dp，从后往前dp。每次看前一列的上下三行。

#### [2707. Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/description/), [Solution](DP/Extra_Characters_in_a_String.py)
从每一个下标开始dp。先初始化成dp(start + 1) + 1就是不用当前字母，当前字母就是extra字母了。然后recursion对后面每一个下标看从当前到后面在不在dictionary里，然后更新res。

#### [2742. Painting the Walls](https://leetcode.com/problems/painting-the-walls/description/), [Solution](DP/Painting_the_Walls.py)
dp，dp[i][j]表示第i个wall用paid来做的情况下，完成j个wall的最低cost。可以只用一维来记录。每个dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])，这里等号右边的dp[j]表示上一步的结果。取这个和使用第i个paid的情况下，也就是用cost[i]。用了cost[i]会占用time[i]的时间，所以可以完成当前的wall以及另外time[i]个用free完成的wall。去掉这么多wall，剩下的最低cost再加上cost[i]，和上一步的取更低的那一个，更新下一步。

#### [2750. Ways to Split Array Into Good Subarrays](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/), [Solution](DP/Ways_to_Split_Array_Into_Good_Subarrays.py)
dp题有思路就好做。dp[i]如果是0就没有新的split方法，直接和前一个一样；如果是1那就可以有新的从前一个一后面的那个0开始一直到这个1前面的那个0那么多种方法数，这些加起来。比如10000后面来一个1，那么就有00001，0001,001,01,1这些新的split。

#### [2830. Maximize the Profit as the Salesman](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/description/), [Solution](DP/Maximize_the_Profit_as_the_Salesman.py)
周赛的时候没思路，其实不难，按照结束的house分个类，然后对每个结束的house做dp。先初始化成dp[i - 1]因为可以完全不选以i结尾的offer。然后对每个以i结尾的offer，看dp[start] + gold和dp[i]的大小。

#### [Snowflake String Pattern](https://www.geeksforgeeks.org/number-of-distinct-words-of-size-n-with-at-most-k-contiguous-vowels/), [Solution](DP/String_Pattern)
dp[i][j]表示长度为i的string，最后j位是元音，的组合数。对每个i，dp[i][0]由i - 1的行和初始化。之后根据j和i的相对大小来判断状态转移方程。可以只保留一行作为dp储存，因为只用到了上一行的dp。

#### [Snowflake String Formattion](https://www.1point3acres.com/bbs/thread-929005-1-1.html)
dp[i][j] = 到target的第i个字母，使用的字母到所有word到第j个为止。每一个i，j < i为0，j = i等于dp[i - 1][i - 1] * target[i]在第j个位置出现的次数。j > i，等于dp[i - 1][k] * target[i]在第k个位置出现的次数，对k从i - 1到j求和。

#### [Snowflake Palindrome Sequence](https://leetcode.com/discuss/interview-question/algorithms/202924/ascend-online-assessment-product-of-palindromes#:~:text=Palindromic%20subsequences), [Solution](https://stackoverflow.com/questions/53663721/find-the-maximum-product-of-two-non-overlapping-palindromic-subsequences), [Solution](DP/Palindrome_Sequnce.java)
先dp，找出从i到j中间的最长palindrome的长度。注意dp是在每个对角线上dp。然后以每个下标为分界点，求分界点左右乘积的最大值。

#### [Snowflake Task Scheduling](https://leetcode.com/discuss/interview-question/2775415/SnowFlake-OA), [Solution](DP/Task_Scheduling.java)
dp(i, j)表示第i个task时，还剩j个free time的min cost。每次考虑task i放paid还是free server，paid就cost += c[i]，j += time[i]，free就j -= 1最后i = n的时候如果j < 0就说明这一列不可行，直接返回inf。

#### [Snowflake Paths to a goal](https://zany-fluorine-852.notion.site/snowflakes-oa-f32a12c872344de98837ac986abc850e), [Solution](DP/Paths_to_a_Goal)
dp[i][j]使用到s[i]为止的rl，到达位置j的不同方法数。每一步减去上一个和当前相同方向的方法数，即dp[pre_same[i]][j +- 1]。


---

<div id='Greedy'></div>

## Greedy

#### [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort/description/), [Solution](Greedy/Wiggle_Sort.py)
首先可以直接排个序，然后每隔一位交换相邻数。或者可以每一位上根据奇偶看跟下一位的大小关系来决定是否和下一位交换。

#### [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/), [Solution](Greedy/Non-overlapping_Intervals.py)
先按结束时间排序，然后依次检测，如果下一个的开始时间大于等于前一个的结束时间，就不去掉，否则去掉这一个。这样相当于在两个重叠的里面保留了结束时间更早的那个，这样就给后面的留了更多空间。

#### [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/description/), [Solution](Greedy/Validate_Stack_Sequences.py)
依次push，只要stack末尾和pop匹配上就pop，直到不匹配，然后push下一个。最后检测stack是否为空。

#### [1402. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/description/), [Solution](Greedy/Reducing_Dishes.py)
排序。0和正数肯定要选，这之后每加一个负数，相当于增加前面所有正数的和，并减去到目前为止加进来的所有负数以及当前这个负数。所以从绝对值小到大开始对负数求和，直到减去的量大于等于正数的增量为止。记录下标，并计算从这个下标开始取的结果。

#### [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/description/), [Solution](Greedy/Maximum_Running_Time_of_N_Computers.py)
先排序，然后把最大的n个电池分配出去。把剩下的加起来，然后对使用中的那n个电池从小到大，依次用剩余的电池把第0到第i个电池的容量补到第i + 1个那么多。这样电脑就可以运行i+1那么长时间。如果一直到最后还有剩余或者中间停住不能补到下一个，就把剩余的所有电量平均分配到所有电池或者前i个电池上。

#### [2193. Minimum Number of Moves to Make Palindrome](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/), [Solution](Greedy/Minimum_Number_of_Moves_to_Make_Palindrome.py)
只用看从末尾开始，把每个对应的字母从原始位置移动到开头的消耗就行。

#### [2366. Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/), [Solution](Greedy/Minimum_Replacements_to_Sort_the_Array.py)
从后往前，依次把每一个比后面大的元素分拆。如果当前的整除后一个就分拆成所有都和后一个一样大，或者不能整除就分成比整除向下取整多一个，就是尽量少的分拆但是每一个都比后面的小。

#### [2573. Find the String with LCP](https://leetcode.com/problems/find-the-string-with-lcp/description/), [Solution](Greedy/Find_the_String_with_LCP.py)
greedy的根据lcp依次填满res列表，如果用到的字符数超过26就返回''，如果遇到已经填过的就跳过。然后再循环一次检查生成的res是否符合lcp。一个个位置对应检查太慢了，所以用lcp[i][j]和lcp[i + 1][j + 1]之间的关系来检查。如果res[i] == res[j]那么lcp[i][j] = lcp[i + 1][j + 1] + 1。最后根据res拼接出答案。

#### [2589. Minimum Time to Complete All Tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description/), [Solution](Greedy/Minimum_Time_to_Complete_All_Tasks.py)
按结束时间排序。这样从结束时间开始往前安排task，可以让后面的task最大化利用前面的时间。然后后面每次过一遍start到end，去掉已经安排过的时间点，然后再从后往前把剩下的时间安排完。

#### [2611. Mice and Cheese](https://leetcode.com/problems/mice-and-cheese/description/), [Solution](Greedy/Mice_and_Cheese.py)
总和 = sum ai + sum bj 其中I大小为k = sum ai - sum bi + sum b这里sum b是直接求和，所以是固定值，只需要最大化 sum ai - sum bi，就是算一下差值，取最大的k个就行了。

#### [2800. Shortest String That Contains Three Strings](https://leetcode.com/problems/shortest-string-that-contains-three-strings/description/), [Solution](Greedy/Shortest_String_That_Contains_Three_Strings.py)
枚举所有string的组合，然后写一个helper找出两个string能重叠的最小super string。然后求super(a, b)，返回的string再和c求一次super。返回所有这些33super里最小的那个。



---

<div id='SQL'></div>

## SQL

#### [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/description/), [Solution](SQL/Combine_Two_Tables.py)
基本sql语法，select join。

#### [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/), [Solution](SQL/Second_Highest_Salary.py)
先找到最大值，然后以这个为条件，在小于他的值里面再找最大值。

#### [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/description/), [Solution](SQL/Nth_Highest_Salary.py)
创建函数的语法，create function 函数名（变量名 变量类型） return 返回类型，begin end，中间return（），括号里写查询语句。limit x，y表示从下标x开始取y个。

#### [178. Rank Scores](https://leetcode.com/problems/rank-scores/description/), [Solution](SQL/Rank_Scores.py)
重命名一个叫S1，从里面选两列，一个score，另一个是rank。rank是另一个distinct copy，S2里面每个行大于等于S1的个数。

#### [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/description/), [Solution](SQL/Consecutive_Numbers.py)
做三个copy，选择里面id依次加一且num相等的distinct的num的个数。

#### [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/), [Solution](SQL/Employees_Earning_More_Than_Their_Managers.py)
建两个copy，然后比较他们的salary，且e1的manageID等于e2的id。

#### [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/), [Solution](SQL/Duplicate_Emails.py)
where用在输出结果之前，用来约束结果；having用在输出结果之后，用来筛选结果。having通常在group by之后。

#### [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/description/), [Solution](SQL/Customers_Who_Never_Order.py)
注意用选出来的表来看in。

#### [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/description/), [Solution](SQL/Department_Highest_Salary.py)
从按department id拼起来的表里取department name，employee name，employee salary。取的行要满足department id和salary的组合是department的最大salary。

#### [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/), [Solution](SQL/Department_Top_Three_Salaries.py)
从拼起来的表里面，选出那些在同样的id里面，大于该项的不超过三个的那些项。

#### [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/), [Solution](SQL/Delete_Duplicate_Emails.py)
选两个copy，删掉第一个里面的所有列，如果email相同且id大于第二个里的。

#### [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/description/), [Solution](SQL/Rising_Temperature.py)
也可以用join。另外比较日期大小应该用DATEDIFF。

#### [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/description/), [Solution](SQL/Game_Play_Analysis_I.py)
简单，用MIN函数。

#### [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/), [Solution](SQL/Managers_with_at_Least_5_Direct_Reports)
注意别名要在括号外面。

#### [574. Winning Candidate](https://leetcode.com/problems/winning-candidate/description/), [Solution](SQL/Winning_Candidate.py)
取第几大的用order by之后limit来取。

#### [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/description/), [Solution](SQL/Employee_Bonus.py)
直接用outer join会报错，必须left或者right。

#### [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/description/), [Solution](SQL/Find_Customer_Referee.py)
mySQL有三个逻辑值，TRUE, FALSE, UNKNOWN。只有TRUE会被where返回。所有和null比较的都是UNKNOWN，不会被返回。所以要额外加一个判断IS NULL。

#### [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/), [Solution](SQL/Customer_Placing_the_Largest_Number_of_Orders.py)
先group了再order。

#### [595. Big Countries](https://leetcode.com/problems/big-countries/description/), [Solution](SQL/Big_Countries.py)
直接选。

#### [607. Sales Person](https://leetcode.com/problems/sales-person/description/), [Solution](SQL/Sales_Person.py)
join选出order里面company为RED的那些的sales_id，然后在salesperson里面找不在这些id里面的人。

#### [608. Tree Node](https://leetcode.com/problems/tree-node/description/), [Solution](SQL/Tree_Node.py)
可以用union把三个情况拼起来，也可以用case when then来作为选出来的那个column。

#### [627. Swap Salary](https://leetcode.com/problems/swap-salary/description/), [Solution](SQL/Swap_Salary.py)
条件语句，case when condition then result 可以多个when then，最后end结束。

#### [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/), [Solution](SQL/User_Activity_for_the_Past_30_Days_I.py)
注意判断大小不能用连续不等号。日期函数是DATEDIFF。

#### [1148. Article Views I](https://leetcode.com/problems/article-views-i/description/), [Solution](SQL/Article_Views_I.py)
基本select。

#### [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/description/), [Solution](SQL/Group_Sold_Products_By_The_Date.py)
GROUP_CONCAT可以返回用逗号连接的字符串。

#### [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description/), [Solution](SQL/Patients_With_a_Condition.py)
用LIKE进行字符串匹配。sql里字符串用单引号，%表示任意字符。

#### [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/), [Solution](SQL/Customer_Who_Visited_but_Did_Not_Make_Any_Transactions.py)
选出在visit但不在transactions里面的那些visit id，然后取对应的customer id，count，group by customer id。

#### [1667. Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/), [Solution](SQL/Fix_Names_in_a_Table.py)
CONCAT函数连接字符串，SUBSTRING(string, startIndex, length of substring)取子串。注意startindex从1开始。

#### [1693. Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/description/), [Solution](SQL/Daily_Leads_and_Partners.py)
group by可以按多个关键字group。

#### [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/description/), [Solution](SQL/Find_Followers_Count.py)
简单。

#### [1741. Find Total Time Spent by Each Employee](https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/), [Solution](SQL/Find_Total_Time_Spent_by_Each_Employee.py)
select列的时候可以直接做计算。然后求sum。

#### [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/), [Solution](SQL/Recyclable_and_Low_Fat_Products.py)
easy，直接select。

#### [1795. Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/description/), [Solution](SQL/Rearrange_Products_Table.py)
用字符串建立新column。然后把三个表UNION起来。

#### [1873. Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/description/), [Solution](SQL/Calculate_Special_Bonus.py)
用IF(conditaion, if true, else)的函数可以直接选出一列

#### [1890. The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/description/), [Solution](SQL/The_Latest_Login_in_2020.py)
用MAX。YEAR可以取出date里的年份。

#### [1965. Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/description/), [Solution](SQL/Employees_With_Missing_Information.py)
left join之后用where筛选里面没有的employee_id。



---

<div id='OOD'></div>

## OOD


#### [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/description/), [Solution](OOD/Robot_Room_Cleaner.py)
往前走，碰到墙或者已经visit过的就右转，四个方向都完了就返回上一个cell。需要另外写一个goBack和dfs函数。


#### [1603. Design Parking System](https://leetcode.com/problems/design-parking-system/description/), [Solution](OOD/Design_Parking_System)
简单。