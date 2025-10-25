package day10;

public class CheckArraySorted {
    public boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true; // If loop completes, array is sorted
    }

    public static void main(String[] args) {
        CheckArraySorted checkArraySorted = new CheckArraySorted();
        System.out.println(checkArraySorted.isSorted(new int[]{10, 20, 30, 40, 50})); // true
        System.out.println(checkArraySorted.isSorted(new int[]{90, 80, 100, 70, 40, 30})); // false
    }
}
