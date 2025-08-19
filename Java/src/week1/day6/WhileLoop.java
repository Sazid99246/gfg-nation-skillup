package week1.day6;

import java.util.*;

public class WhileLoop {
    public static void solve() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        while(n >= 0) {
            System.out.printf("%d ", n);
            n--;
        }
    }

    public static void main(String[] args) {
        solve();
    }
}