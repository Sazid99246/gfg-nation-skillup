package week2.day8;

public class PrimeFactorization {
    public static void printPrimeFactorization(int n) {
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                System.out.print(i + " ");
                n /= i;
            }
        }

        if (n > 1) {
            System.out.print(n);
        }
    }

    public static void main(String[] args) {
        printPrimeFactorization(100);
    }
}
