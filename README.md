# LeetCode Problems

## ✅ Solved Problems

| # | Title | Topic | Time | Notes |
|---|------|------|------|------|
| 42 | Trapping Rain Water | Array / Prefix-Suffix | O(n) | Precompute left and right maximum heights in separate arrays. Then check minimum height and subtract from actual height. Sum of these differences gives you the answer. |
| 1944 | Number of Visible People in a Queue | Monotonic Stack | O(n) | Traverse from right; pop shorter heights (visible) and count first taller blocker. Use a stack with following steps, keep on popping elements from stack until you find an element thats smaller than the peek element in stack. Keep on updating count as it will give the total no. of people in between. Also add one to count if stack is not empty yet since it gives you the count of blocker as well. Update the value in result array and push current index to stack. |
