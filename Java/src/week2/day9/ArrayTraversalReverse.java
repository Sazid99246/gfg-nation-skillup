package week2.day9;

class Solution {
    public static void arrayTraversalReverse(int[] arr) {
        String result = "";

        for (int i = arr.length - 1; i >= 0; i--) {
            result += arr[i];
            if (i > 0) {
                result += " ";
            }
        }

        System.out.print(result);
    }
}

public class ArrayTraversalReverse {
    public static void main(String[] args) {
        Solution s = new Solution();
        Solution.arrayTraversalReverse(new int[]{54, 43, 2, 1, 5});
    }
}
