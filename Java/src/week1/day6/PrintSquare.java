package week1.day6;

import java.util.*;

public class PrintSquare {
    public static void solve() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n - 1; i++) {
            System.out.printf("%s ","*");
        }
        System.out.println("*");

        for (int i = 0; i < n - 2; i++) {
            System.out.print("* ");
            for (int j = 0; j < n - 2; j++) {
                System.out.print("  ");
            }
            System.out.println("*");
        }

        for (int i = 0; i < n - 1; i++) {
            System.out.printf("%s ", "*");
        }
        System.out.println("*");
    }

    public static void main(String[] args) {
        solve();
    }
}