## What's the lab about?

This lab involves developing some divide and conquer algorithms, to solve the maximum segment sum problem.

Suppose you are given a list of integers (so some might be negative). The maximum segment sum of the list is the contiguous sublist whose sum is the largest. (Note that there's an ambiguity if there are 0s in the list; these are not usually counted in the maximum segment, so we're actually looking for the shortest sequence with the largest sum.)

For example if the list is [2 4 5 -7 3 -6 1 4], then the maximum segment sum is 11 and the corresponding segment is [2 4 5]. Notice that negative numbers don't necessary act as stoppers to maximum segments if the sums on both sides are large.

There's an obvious O(n^2) algorithm: check the segment sum between every possible start and end position. But the goal is to develop a divide and conquer algorithm.

As usual, we will divide the list in half recursively; and the base case will be the segment sum of whatever short sequence you choose to stop at. But the key insight is that, if every recursive call returns information about the maximum segment sum it contains and the maximum sums that end at its right and left ends, then these results from the two children can be assembled into the same information to pass upwards. At the top level of the recursion, the contained maximum segment sum is the desired answer. (This should remind you of the maximum path in an unrooted tree problem, but in this case each recursive call can't tell if it's a left or a right child of its parent and so has to keep track of the segments that end at both left and right.)

### Part 1
   Build an implementation of mss using this strategy. So that you can't just copy one of the many thousands of implementations from the Web, let's solve this specialised version: given a list of integers whose length is n, compute the maximum segment sum and the elements of the maximum segment between given positions left < right <= n.

   Test your code convincingly, i.e. with at least some examples where the maximum segment contains negative numbers and where the maximum segment is the entire sublist.

   What is the complexity of your solution?

### Part 2
   Suppose that you wanted to find the two maximal non-overlapping segments. One approach would be to find the maximal one, replace all the entries from the maximal segment with a suitably small value, and then run the algorithm again.

   Implement this idea, justifying your choice of replacement value. (Note that idea extends to the k maximal segments as long as they are non-overlapping.) What is the complexity?

### Part 3
   If you have time, think about how to find the two largest segments if they're allowed to be overlapping. (and build an implementation if you can). What is the complexity?
