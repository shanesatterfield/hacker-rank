import java.util.*;

public class Solution {
    public static void main(String[] args) {
        scan = new Scanner(System.in);

        int testCases = 0;
        if (scan.hasNextInt()) {
            testCases = scan.nextInt();
        }

        for (int i = 0; i < testCases; ++i) {
            System.out.println(handshakes(scan.nextInt()));
        }
    }

    public static int handshakes(int people) {
        if (people <= 0) {
            return 0;
        }

        return people * (people-1) / 2;
    }

    public static Scanner scan;
}
