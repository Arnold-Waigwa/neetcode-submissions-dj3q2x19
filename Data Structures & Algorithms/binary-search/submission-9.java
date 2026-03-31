class Solution {
    public int search(int[] nums, int target) {
        return dfs(0, nums.length - 1, nums, target);
    }
        
    private int dfs(int l, int r, int[] nums, int target) {
        if (l > r) return -1;
        int mid = (l + r) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] > target){
            return dfs(l, mid - 1, nums, target);
        }
        else {
            return dfs(mid + 1, r, nums, target);
        }
    
    }
    

}
