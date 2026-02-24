package leetcode;
/*
    42 - Trapping Rain Water
    Topic: Array / Prefix-Suffix
    Time: O(n)
    Notes: Precompute left and right maximum heights in separate arrays. Then check minimum height and subtract from actual height. Sum of these differences gives you the answer.
*/
public class _0042_Trapping_Rain_Water {
    public int trap(int[] height) {
        int max = height[0], n = height.length;
        int[] forth = new int[n];
        for(int i=0; i<n; i++){
            max = Math.max(max, height[i]);
            forth[i] = max;
        }
        max = height[n-1];
        int[] back = new int[n];
        for(int i=n-1; i>=0; i--){
            max = Math.max(max, height[i]);
            back[i] = max;
        }

        int result = 0;
        for(int i=0; i<n; i++){
            int diff = Math.min(forth[i],back[i]);
            result += diff - height[i];
        }
        return result;
    }
}
