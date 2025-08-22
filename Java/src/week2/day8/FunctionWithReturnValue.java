package week2.day8;

public class FunctionWithReturnValue {
    int returnValueFunction(int n) {
        return n * 2;
    }

    public static void main(String[] args) {
        FunctionWithReturnValue f = new FunctionWithReturnValue();
        System.out.println(f.returnValueFunction(5));
    }
}