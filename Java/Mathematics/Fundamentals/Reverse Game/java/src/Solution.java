import java.util.*;

public class Solution {
    public static void main(String args[]) {
        scan = new Scanner(System.in);

        int testCases = 0;
        if (scan.hasNextInt()) {
            testCases = scan.nextInt();
        }

        for (int i = 0; i < testCases; ++i) {
            System.out.println(reverseGame(scan.nextInt(), scan.nextInt()));
        }
    }

    public static int reverseGame(int N, int K) {
        N -= 1;
        if (K >= N / 2) {
            return (N-K)*2;
        }
        return K*2+1;
    }

    public static Scanner scan;
}
