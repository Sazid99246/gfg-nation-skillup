package day12;

public class CheckPalindrome {
    public static boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String s2 = new StringBuilder(s).reverse().toString();
        
        return s.equals(s2);
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("Hello"));
        System.out.println(isPalindrome("TenEt"));
    }
}
