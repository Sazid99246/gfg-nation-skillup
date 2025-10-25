package day10;

import java.util.Arrays;

public class DecrementArrayValues {
    public static int[] decrementArrayElements(int[] arr) {
        int[] newArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i] - 1;
        }
        return newArr;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(decrementArrayElements(new int[]{54, 43, 2, 1, 5})));
        System.out.println(Arrays.toString(decrementArrayElements(new int[]{324, 5, 2, 2})));
    }
}
