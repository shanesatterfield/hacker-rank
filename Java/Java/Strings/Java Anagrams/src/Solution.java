import java.util.*;

public class Solution {
    public static void main(String args[]) {
        scan = new Scanner(System.in);

        Anagram ana1 = new Anagram(scan.nextLine());
        Anagram ana2 = new Anagram(scan.nextLine());

        boolean result = ana1.isAnagram(ana2);
        String output = "Anagrams";
        if (result == false) {
            output = "Not Anagrams";
        }

        System.out.println(output);
    }

    private static Scanner scan;
}
