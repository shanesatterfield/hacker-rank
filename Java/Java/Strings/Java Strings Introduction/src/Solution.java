import java.util.Scanner;

/**
 * Java Strings Introduction Solution
 */
public class Solution {

    public static void main(final String args[]) {
        final Scanner scan = new Scanner(System.in);
        final String a = scan.next();
        final String b = scan.next();

        System.out.println(combinedLength(a, b));
        System.out.println(alphabetical(a, b) ? "Yes" : "No");
        System.out.println(concat(a, b));
    }


    public static int combinedLength(final String a, final String b) {
        return a.length() + b.length();
    }


    public static boolean alphabetical(final String a, final String b) {
        return a.compareTo(b) > 0;
    }


    public static String concat(final String a, final String b) {
        return String.format("%s %s", capitalize(a), capitalize(b));
    }


    public static String capitalize(final String str) {
        final char head = Character.toUpperCase(str.charAt(0));
        final String tail;

        if (str.length() > 1) {
            tail = str.substring(1, str.length());
        }
        else {
            tail = "";
        }

        return head + tail;
    }
}
