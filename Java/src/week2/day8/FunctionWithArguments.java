package week2.day8;

public class FunctionWithArguments {
    int argumentFunction(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        FunctionWithArguments f = new FunctionWithArguments();
        System.out.println(f.argumentFunction(1, 2));
    }
}
