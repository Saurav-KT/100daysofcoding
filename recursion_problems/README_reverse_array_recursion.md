arr = [20, 36, 19, 46]
PART 1: reverse_array (REMOVING elements)
Think of this as removing elements until only one is left.

Step 1

`temp = 46
arr  = [20, 36, 19]`

Step 2

`temp = 19
arr  = [20, 36]`

Step 3

`temp = 36
arr  = [20]`

Step 4 (base case)

`arr = [20]   # stop recursion`

At this point, All other elements are saved in the call stack.The list has only one element.

PART 2: insert_at_bottom (PUTTING elements BACK)
Now recursion comes back and inserts elements at the bottom.

Insert 36 at bottom of [20]
Before insert

`[20]`

Remove 20

`[]`

Insert 36

`[36]`

Put back 20

`[36, 20]`

Insert 19 at bottom of [36, 20]
Remove 20

`[36]`

Remove 36

`[]`

Insert 19

`[19]`

Put back 36

`[19, 36]`

Put back 20

`[19, 36, 20]`

Insert 46 at bottom of [19, 36, 20]
Remove 20

`[19, 36]`

Remove 36
[19]

Remove 19
[]

Insert 46
`[46]`

Put back 19
`[46, 19]`

Put back 36
`[46, 19, 36]`

Put back 20
`[46, 19, 36, 20]`

FINAL ARRAY
`[46, 19, 36, 20]`

First recursion removes everything
Second recursion rebuilds the list from the bottom

reverse_array([20,36,19,46])

Step1 till Basecase

┌────────────────────────────┐
│ reverse_array([20])         │
├────────────────────────────┤
│ reverse_array([20,36])      │
├────────────────────────────┤
│ reverse_array([20,36,19])   │
├────────────────────────────┤
│ reverse_array([20,36,19,46]) │
└────────────────────────────┘

PART 2: STACK UNWINDING (INSERT AT BOTTOM)
Now recursion returns upward.

Takeaway

reverse_array removes elements going DOWN
insert_at_bottom rebuilds the list coming UP

    