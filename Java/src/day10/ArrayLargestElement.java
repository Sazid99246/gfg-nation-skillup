package day10;

public class ArrayLargestElement {
    public static int largest(int[] arr) {
        int largest = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        System.out.println(largest(new int[]{1, 8, 7, 56, 90}));
        System.out.println(largest(new int[]{5, 5, 5, 5}));
        System.out.println(largest(new int[]{10}));
    }
}
