package day12;

public class PangramChecker {
    public static boolean isPangram(String str) {
        // Convert to lowercase for consistency
        str = str.toLowerCase();

        // Create a boolean array to track all 26 letters
        boolean[] letters = new boolean[26];

        // Mark letters that appear
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                letters[ch - 'a'] = true;
            }
        }

        // Check if all 26 letters are present
        for (boolean present : letters) {
            if (!present) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String sentence = "The quick brown fox jumps over the lazy dog";
        System.out.println(isPangram(sentence)); // true
    }
}
