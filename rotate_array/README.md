### Rotate Array

Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer.
Do the mentioned change in the array in place.
Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

solution:

reverse(0, d-1) → reverse(d, n-1) → reverse(all)
reverse(0, d-1)
Step 1: Reverse first d elements
Reverse [1, 2] → [2, 1]
Array becomes: [2, 1, 3, 4, 5]

Step 2: Reverse remaining n-d elements
reverse(d, n-1)  # reverse(2, 4)
Reverse [3, 4, 5] → [5, 4, 3]
Array becomes: [2, 1, 5, 4, 3]

Step 3: Reverse the entire array
reverse(0, n-1)  # reverse(0, 4)
Reverse [2, 1, 5, 4, 3] → [3, 4, 5, 1, 2]
Final result: [3, 4, 5, 1, 2]

