import java.util.*;

public class Solution {
    public static void main(String args[]) {
        if (scan == null) {
            scan = new Scanner(System.in);
        }

        if(scan.hasNextInt()) {
            int testCases = scan.nextInt();
            int a, b;
            for (int i = 0; i < testCases; ++i) {
                a = scan.nextInt();
                b = scan.nextInt();

                System.out.println(getSlices(a, b));
            }
        }
    }

    public static int getSlices(int a, int b) {
        return a * b / (int) Math.pow(gcd(a, b), 2);
    }

    public static int gcd(int a, int b) {
        if (a == b) {
            return a;
        }

        return gcd(Math.min(a,b), Math.abs(b-a));
    }

    private static Scanner scan;
}
