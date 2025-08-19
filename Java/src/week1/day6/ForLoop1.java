package week1.day6;

import java.util.*;

public class ForLoop1 {
    public static void solve() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();


        for(int i = 1; i < 10; i++) {
            System.out.printf("%d ", n * i);
        }
        System.out.println(n * 10);
    }

    public static void main(String[] args) {
        solve();
    }
}