import java.util.Scanner;

public class Solution {
    public static void main(String args[]) {
        Scanner scan     = new Scanner(System.in);
        PrimesFinder pf  = new PrimesFinder();
        int numTestCases = scan.nextInt();
        int testCase     = 0;

        for (int i = 0; i < numTestCases; ++i) {
            testCase = scan.nextInt();
            System.out.println(pf.getPrime(testCase));
        }
    }
}
