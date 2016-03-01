import java.util.*;

public class Solution {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        System.out.println(diamond(scan.nextInt()));
    }

    public static String diamond(int num) {
        if (num % 2 != 0 || num >= 6 && num <= 20) {
            return "Weird";
        }
        else if (num >= 2 && num <= 5 || num > 20) {
            return "Not Weird";
        }
        return null;
    }
}
