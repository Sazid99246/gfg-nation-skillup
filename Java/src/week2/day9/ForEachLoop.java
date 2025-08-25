package week2.day9;

public class ForEachLoop {
    public void printArray(String[] arr) {
        for (String s: arr) {
            System.out.println(s);
        }
    }

    public static void main(String[] args) {
        String[] arr = {"Hello", "World", "Geeks,", "For", "Geeks"};
        ForEachLoop obj = new ForEachLoop();
        obj.printArray(arr);
    }
}