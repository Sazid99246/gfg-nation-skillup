package week1.day6;

// User function Template for Java
public class FizzBuzz {
    public static void fizzBuzz(int number) {
        if (number % 3 == 0 && number % 5 == 0) {
            System.out.println("FizzBuzz");
        } else if (number % 3 == 0) {
            System.out.println("Fizz");
        } else if (number % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(number);
        }
    }

    public static void main(String[] args) {
        fizzBuzz(3);
        fizzBuzz(5);
        fizzBuzz(15);
    }
}