package week2.day8;

public class FirstDigitOfNumber {
    public static int firstDigit(int n) {
        while (n > 9) {
            n /= 10;
        }
        return n;
    }

    public static void main(String[] args) {
        System.out.println(firstDigit(123));
    }
}