import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.stream.Collectors;
import java.text.*;
import java.math.*;
import java.util.regex.*;


/**
 * Solution for Java - Advanced - Java Varargs.
 *
 * You are given a class Solution and its main method in the editor. Your task is to create
 * the class Add and the required methods so that the code prints the sum of the numbers
 * passed to the function add.
 *
 * Note: Your add method in the Add class must print the sum as given in the Sample Output
 */
class Add {

    /**
     * Print a string in the form of "1+2+3=6" based on the arguments given.
     *
     * @param args A list of integers used to construct the equation and find the sum.
     */
    public void add(final int ...args) {

        final String equation = buildEquation(args);
        final int sum = Arrays.stream(args).sum();

        System.out.printf("%s=%d\n", equation, sum);
    }


    /**
     * Build the equation portion of the add function's string.
     * This builds the "1+2+3" portion.
     *
     * @param args An array of arguments that will be concatenated for the equation string.
     * @return The arguments concatenated with "+", which results in the equation string.
     */
    private String buildEquation(final int[] args) {

        return Arrays.stream(args)
                     .mapToObj(Integer::toString)
                     .collect(Collectors.joining("+"));
    }
}

/**
 * The code below is provided by the test case.
 * I have formatted the code below for consistent coding style.
 */
public class Solution {

    public static void main(final String[] args) {

        try {

            // Read input from stdin.
            final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            final int n1 = Integer.parseInt(br.readLine());
            final int n2 = Integer.parseInt(br.readLine());
            final int n3 = Integer.parseInt(br.readLine());
            final int n4 = Integer.parseInt(br.readLine());
            final int n5 = Integer.parseInt(br.readLine());
            final int n6 = Integer.parseInt(br.readLine());

            // Apply inputs to the Add class, which prints the output.
            final Add ob = new Add();
            ob.add(n1, n2);
            ob.add(n1, n2, n3);
            ob.add(n1, n2, n3, n4, n5);
            ob.add(n1, n2, n3, n4, n5, n6);

            // Check if the method was overloaded. This is to make sure varargs were used.
            final Method[] methods = Add.class.getDeclaredMethods();
            final Set<String> set = new HashSet<>();
            boolean overload = false;

            for (int i = 0; i < methods.length; i++) {

                if (set.contains(methods[i].getName())) {
                    overload = true;
                    break;
                }

                set.add(methods[i].getName());
            }

            if (overload) {
                throw new Exception("Overloading not allowed");
            }
        }
        catch (final Exception e) {
            e.printStackTrace();
        }
    }
}
