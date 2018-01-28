import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(final String args[]) {
        final Scanner scanner = new Scanner(System.in);
        final int N = scanner.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.println(buildLine(N, i));
        }
    }

    public static String buildLine(final int a, final int b) {
        final int mult = a * b;
        return String.format("%d x %d = %d", a, b, mult);
    }
}
