package day15;

public class Addition {
    public static int add(int a, int b) {
        return a + b;
    }

    static void printSum(int... nums) {
        int sum = 0;
        for (int n : nums)
            sum += n;
        System.out.println(sum);
    }

    public static void main(String[] args) {
        System.out.println(add(2, 3));
    }
}
