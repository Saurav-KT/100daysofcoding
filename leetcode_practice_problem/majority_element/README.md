### Boyer-Moore Majority Voting Algorithm

The Boyer–Moore Majority Vote algorithm finds the majority element in 
an array — an element that appears more than ⌊n / 2⌋ times.

Why verification is needed?

The Boyer–Moore algorithm always returns a candidate, even when no majority element exists.

It only guarantees correctness if a majority (> n/2) is guaranteed to exist.

The candidate changes whenever count drops to 0.
That means:
The current candidate has been “cancelled out” by other elements
The next element becomes the new candidate
Intuition (Cancellation Logic)
Think of it as:
Each different element cancels one occurrence of the candidate.
If candidate survives all cancellations, it must be the majority.
The true majority element cannot be fully cancelled.


