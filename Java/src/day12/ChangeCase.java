package day12;

public class ChangeCase {
    public static void changeCase(String s) {
        System.out.println(s.substring(0, 1).toUpperCase() + s.substring(1));
        System.out.println(s.toUpperCase());
    }

    public static void main(String[] args) {
        changeCase("hello");
        changeCase("world");
    }
}
