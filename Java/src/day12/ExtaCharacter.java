package day12;

import java.util.Arrays;

public class ExtaCharacter {
    public static char extraChar(String s1, String s2) {
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                return arr2[i]; // the extra char is in s2
            }
        }

        // If no mismatch found, the extra character is the last one in s2
        return arr2[arr2.length - 1];
    }

    public static void main(String[] args) {
        String s1 = "abcd";
        String s2 = "abcde";
        System.out.println(extraChar(s1, s2)); // Output: e
    }
}
