import java.io.*;
import java.util.*;

/**
 * Java Loops
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Get the number of test cases and run the test cases through the code.
        int testCases = Integer.parseInt(br.readLine());
        for( int i = 0; i < testCases; ++i ) {
            // Get the input and parse it into the proper format.
            int[] nums = getLine( br.readLine() );

            // Take the input and calculate the answers.
            List<Integer> ans = genAnsList( nums );

            // Print the answers
            for( int j = 0; j < ans.size(); ++j ) {
                System.out.printf("%d ", ans.get(j));
            }
            System.out.println();
        }

        br.close();
    }

    /**
     * Generates an Integer List containing the answers.
     * @param nums A series of three numbers specified by the prompt.
     * @return The answer to the problem as a list of Integer objects.
     */
    public static List<Integer> genAnsList( int[] nums ) {
        // Creates the list for the answers and inserts the first element into it for ease of use.
        List<Integer> ans = new ArrayList<Integer>();
        ans.add( nums[0] );

        for( int i = 0; i < nums[2]; ++i ) {
            ans.add( ans.get(i) + (int)(Math.pow(2, i)) * nums[1] );
        }

        // Remove the first element that was added in only for convenience.
        ans.remove( 0 );

        return ans;
    }

    /**
     * Takes a String input and splits it into the proper Integers.
     * @param line The String that will be parsed.
     * @return An array of 3 integers as specified by the problem statement.
     */
    public static int[] getLine( String line ) {
        String[] temp = line.split(" ");
        int[] nums = new int[temp.length];

        for( int i = 0; i < nums.length; ++i  ) {
            nums[i] = Integer.parseInt( temp[i] );
        }

        return nums;
    }
}
