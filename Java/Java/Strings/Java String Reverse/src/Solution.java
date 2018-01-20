import java.util.*;

public class Solution {
    public static void main(String args[]) {
        scan           = new Scanner(System.in);
        boolean result = isPalindrome(scan.nextLine());

        String output = "Yes";
        if (!result) {
            output = "No";
        }

        System.out.println(output);
    }

    public static boolean isPalindrome(String str) {
        boolean result = true;
        for (int i = 0; i < str.length()/2; ++i) {
            result = str.charAt(i) == str.charAt(str.length()-1 - i);
            if (result == false) {
                break;
            }
        }
        return result;
    }

    public static Scanner scan;
}
