package week1.day3;

public class DataTypes {

    // Function to do operations with different data types
    static void dataTypes(int a, float b, double c, long l, byte d) {

        double p = c / b; // c/b
        double q = b / a; // b/a
        double r = c / a; // c/a
        double m = r + l; // r+l
        int s = a / d;    // a/d

        // Printing all the results
        System.out.println(p + " " + q + " " + r + " " + m + " " + s);
    }

    public static void main(String[] args) {
        dataTypes(1, 2F, 3.0, 5L, (byte) 127);
    }
}