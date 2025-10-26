package day12;

public class SliceString {
    public static String sliceString(String s) {
        return s.substring(1, s.length()-1);
    }

    public static void main(String[] args) {
        System.out.println(sliceString("Hello"));
    }
}
