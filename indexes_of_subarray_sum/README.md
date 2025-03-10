### Given an array arr[] containing only non-negative integers,
your task is to find a continuous subarray (a contiguous sequence of elements)
whose sum equals a specified value target. You need to return the 1-based indices of
the leftmost and rightmost elements of this subarray. You need to find the first subarray
whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]

Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]

Explanation: There is no subarray with sum 2.

To solve the problem of finding the indices of a subarray whose sum equals a specified target value, we can use the Sliding Window technique. This approach is efficient and works in linear time, making it suitable for large arrays.

Steps to Solve the Problem:
Initialize Two Pointers: Use two pointers, left and right, to represent the current window of the subarray. Both pointers start at the beginning of the array.

Track the Current Sum: Maintain a variable current_sum to keep track of the sum of the elements within the current window.

Expand the Window: Move the right pointer to the right, adding the value at arr[right] to current_sum.

Shrink the Window: If current_sum exceeds the target, move the left pointer to the right, subtracting the value at arr[left] from current_sum.

Check for Target Sum: If current_sum equals the target, return the 1-based indices of the left and right pointers.

Continue Until the End: Repeat the process until the right pointer reaches the end of the array.


Explanation:
Initialization: Start with left = 0 and current_sum = 0.

Expanding the Window: As we iterate through the array, we add each element to current_sum.

Shrinking the Window: If current_sum exceeds the target, we move the left pointer to the right, reducing current_sum by the value at arr[left].

Checking for Target: When current_sum equals the target, we return the 1-based indices of the left and right pointers.

Termination: If no subarray is found, return None.

Time Complexity:
The time complexity is O(n), where n is the number of elements in the array. This is because each element is visited at most twice (once by the right pointer and once by the left pointer).

Space Complexity:
The space complexity is O(1), as we are using only a constant amount of extra space.


Example Walkthrough:
Let’s use the array [1, 2, 3, 4, 5] and target = 9 to see how the sliding window works:

Initial State:

left = 0, right = 0, current_sum = 1 (window: [1]).

current_sum < target, so we expand the window by moving right.

Expand Window:

right = 1, current_sum = 1 + 2 = 3 (window: [1, 2]).

current_sum < target, so we expand again.

Expand Window:

right = 2, current_sum = 3 + 3 = 6 (window: [1, 2, 3]).

current_sum < target, so we expand again.

Expand Window:

right = 3, current_sum = 6 + 4 = 10 (window: [1, 2, 3, 4]).

current_sum > target, so we shrink the window using the while loop.

Shrink Window:

Remove arr[left] = 1 from the window: current_sum = 10 - 1 = 9.

Move left to 1 (window: [2, 3, 4]).

Now, current_sum == target, so we return the indices [2, 4] (1-based).
