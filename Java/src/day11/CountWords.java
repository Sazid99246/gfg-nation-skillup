package day11;

public class CountWords {
    public static int countWords(String str) {
        return str.split(" ").length;
    }

    public static void main(String[] args) {
        System.out.println(countWords("World is hello"));
    }
}
