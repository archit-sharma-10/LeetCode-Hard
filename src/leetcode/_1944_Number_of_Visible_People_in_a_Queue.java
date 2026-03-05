package leetcode;
/*
    1944 - Number of Visible People in a Queue
    Topic: Monotonic Stack
    Time: O(n)
    Notes: Traverse from right; pop shorter heights (visible) and count first taller blocker. Use a stack with following steps, keep on popping elements from stack until you find an element thats smaller than the peek element in stack. Keep on updating count as it will give the total no. of people in between. Also add one to count if stack is not empty yet since it gives you the count of blocker as well. Update the value in result array and push current index to stack.
*/
import java.util.*;
public class _1944_Number_of_Visible_People_in_a_Queue {
    public int[] canSeePersonsCount(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int n = heights.length;
        int[] result = new int[n];
        for(int i=n-1; i>=0; i--){
            int count = 0;
            while(!stack.isEmpty() && heights[i] >= heights[stack.peek()]){
                count++;
                stack.pop();
            }
            if(!stack.isEmpty()) count++;
            result[i] = count;
            stack.push(i);
        }
        return result;
    }
}
