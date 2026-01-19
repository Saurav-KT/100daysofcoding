arr = [3, 1, 4, 2]
sort_arr(arr)

Phase 1: sort_arr() (breaking the array)

Call 1

`sort_arr([3, 1, 4, 2])
temp = 2
arr = [3, 1, 4]`

→ call sort_arr([3, 1, 4])

Call 2

`sort_arr([3, 1, 4])
temp = 4
arr = [3, 1]`

→ call sort_arr([3, 1])

Call 3

`sort_arr([3, 1])
temp = 1
arr = [3]`

→ call sort_arr([3])

Call 4 (Base Case)

`sort_arr([3])
len <= 1 → return`

Now recursion starts returning.
Phase 2: insert() (building sorted array)

insert([3], 1)

`3 > 1 → pop 3
insert([], 1)`

insert([], 1)

`→ append 1
arr = [1]`

Backtrack:

`append 3
arr = [1, 3]`

After Call 3:

`arr = [1, 3]`

Insert temp = 4 into [1, 3]

`insert([1, 3], 4)
3 <= 4 → append 4`

After Call 2:

`arr = [1, 3, 4]`

Insert temp = 2 into [1, 3, 4]

`insert([1, 3, 4], 2)
4 > 2 → pop 4
insert([1, 3], 2)`

3 > 2 → pop 3

`insert([1], 2)`

`1 <= 2 → append 2
arr = [1, 2]`

Backtrack:

`append 3 → [1, 2, 3]
append 4 → [1, 2, 3, 4]`

Final Output

`[1, 2, 3, 4]`


Call Stack Visualization
sort_arr([3,1,4,2])
 └─ sort_arr([3,1,4])
     └─ sort_arr([3,1])
         └─ sort_arr([3])  ← base case

Then insertion happens bottom-up.

Important: 
sort_arr → breaks the problem
insert → fixes the order while returning

Similar to insertion sort using recursion