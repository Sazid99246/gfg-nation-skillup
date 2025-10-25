package day10;

public class Average {
    public static double posAverage(int[] arr) {
        double sum = 0;
        double count = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 0) {
                sum += arr[i];
                count += 1;
            }
        }

        return sum / count;
    }

    public static void main(String[] args) {
        System.out.println(posAverage(new int[]{-12, 8, -7, 6, 12, -9, 14}));
        System.out.println(posAverage(new int[]{1, 2, 3}));
    }
}
