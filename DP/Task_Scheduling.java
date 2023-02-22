import java.util.*;

public class Solution {
    public static class TaskScheduling {
        private static final long INF = Long.MAX_VALUE / 10;
        private static long getMinCost(int[] cost, int[] time) {
            assert cost.length > 0;
            assert cost.length == time.length;
            Map<Integer,Long>[] memo = new Map[cost.length];
            for (int i = 0; i < cost.length; i++) memo[i] = new HashMap<>();
            return dfs(0, cost, 0, time, memo);
        }

        private static long dfs(int i, int[] cost, int timeSoFar, int[] time, Map<Integer,Long>[] memo) {
            int n = cost.length;
            if (i == n) return timeSoFar >= 0 ? 0 : INF;
            if (timeSoFar >= n - i) return 0;
            if (memo[i].containsKey(timeSoFar)) return memo[i].get(timeSoFar);
            long resPaid = cost[i] + dfs(i+1, cost, timeSoFar + time[i], time, memo); // paid server
            long resFree = dfs(i+1, cost, timeSoFar - 1, time, memo); // free server
            memo[i].put(timeSoFar, Math.min(resPaid, resFree));
            return memo[i].get(timeSoFar);
        }
    }

    public static void main(String args[]) {
        int[] cost = {1,2,3,2};
        int[] time = {1,2,3,2};
        System.out.println(TaskScheduling.getMinCost(cost, time));     //3

        cost = new int[]{2, 3, 4, 2};
        time = new int[]{1, 1, 1, 1};
        System.out.println(TaskScheduling.getMinCost(cost, time));     //4

        cost = new int[]{1,1,3,4};
        time = new int[]{3,1,2,3};
        System.out.println(TaskScheduling.getMinCost(cost, time));     //1

        cost = new int[]{10,10,10,10,10,20,20,20};
        time = new int[]{3, 3, 3, 3, 3, 6, 6, 6};
        System.out.println(TaskScheduling.getMinCost(cost, time));     //20

        cost = new int[]{5,6,7,8,8,10};
        time = new int[]{1,1,1,1,1,10};
        System.out.println(TaskScheduling.getMinCost(cost, time));     //10
    }
}