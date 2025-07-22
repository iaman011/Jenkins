// A simple Java program with arithmetic functions and fixed input
public class HelloJava {

    // Main method: Entry point of the program
    public static void main(String[] args) {
        System.out.println("Hello from Java!");

        int a = 10;
        int b = 20;

        System.out.println("Addition: " + add(a, b));
        System.out.println("Subtraction: " + subtract(a, b));
        System.out.println("Multiplication: " + multiply(a, b));
        System.out.println("Division: " + divide(a, b));
    }

    // Function to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    // Function to subtract two numbers
    public static int subtract(int a, int b) {
        return a - b;
    }

    // Function to multiply two numbers
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Function to divide two numbers
    public static double divide(int a, int b) {
        if (b == 0) {
            System.out.println("Error: Division by zero is not allowed.");
            return 0;
        }
        return (double) a / b;
    }
}
