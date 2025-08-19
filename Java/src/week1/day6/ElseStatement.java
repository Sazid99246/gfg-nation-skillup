package week1.day6;

import java.util.*;

public class ElseStatement {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n > 100) {
            System.out.println("Big");
        } else {
            System.out.println("Number");
        }
    }
}