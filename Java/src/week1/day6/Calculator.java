package week1.day6;

public class Calculator {
    public static void utility(int a, int b, int opr) {
        String result;
        if (opr == 1) {
            result = String.valueOf(a + b);
            System.out.print(result);
        } else if (opr == 2) {
            result = String.valueOf(a - b);
            System.out.print(result);
        } else if (opr == 3) {
            result = String.valueOf(a * b);
            System.out.print(result);
        } else {
            System.out.print("Invalid Input");
        }
    }

    public static void main(String[] args) {
        utility(1, 2, 3);
    }
}