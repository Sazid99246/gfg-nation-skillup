package week1.day5;

import java.util.Arrays;

public class ArithmeticOperators {
    public int[] computeOperations(int x, int y) {
        int[] result = new int[5];

        result[0] = x + y;
        result[1] = x - y;
        result[2] = x * y;
        result[3] = x / y;
        result[4] = x % y;

        return result;
    }

    public static void main(String[] args) {
        ArithmeticOperators a = new ArithmeticOperators();
        int[] result = a.computeOperations(10, 20);
        System.out.println(Arrays.toString(result));
    }
}
