package day10;

public class SumOfAllNumbers {
    public static int arraySum(int[] arr) {
        int sum = 0;

        for (int i : arr) {
            sum += i;
        }

        return sum;
    }

    public static void main(String[] args) {
        System.out.println(arraySum(new int[]{54, 43, 2, 1, 5}));
        System.out.println(arraySum(new int[]{324, 5, 2, 2}));
    }
}
