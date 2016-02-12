import java.util.*;
import java.io.*;

/**
 * Solution for Java -> Data Structures -> Java 1D Array (Easy)
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        System.out.println( calcSubListSums( getInput() ) );
    }

    /**
     * @param  nums A list to find the sum of.
     * @return      The sum of the list passed into the method.
     */
    public static int sum( List<Integer> nums ) {
        int total = 0;
        for( int i = 0; i < nums.size(); ++i ) {
            total += nums.get( i );
        }
        return total;
    }

    /**
     * Takes a list and separates it into all possible sublists and returns the
     * of sublists that have a negative sum;
     * @param  nums A list that will be separated into sublists.
     * @return      The number of sublists that have a negative sum.
     */
    public static int calcSubListSums( List<Integer> nums ) {
        int count = 0;

        for( int i = 0; i < nums.size(); ++i ) {
            for( int j = i; j < nums.size(); ++j ) {
                List<Integer> temp = nums.subList(i, j+1);
                if( sum(temp) < 0 ) {
                    count += 1;
                }
            }
        }

        return count;
    }

    /**
     * @return A list of integers read from stdin.
     */
    public static List<Integer> getInput() {
        List<Integer> nums = new ArrayList<Integer>();
        BufferedReader br = null;

        try {

            br = new BufferedReader(new InputStreamReader(System.in));
            int testCases = Integer.parseInt( br.readLine() );

            String[] stringNums = br.readLine().split(" ");
            for( int i = 0; i < stringNums.length; ++i ) {
                nums.add( Integer.parseInt(stringNums[i]) );
            }

        } catch( IOException e) { e.printStackTrace(); }
        finally {
            if( br != null ) {
                try { br.close(); } catch( IOException e ) { e.printStackTrace(); }
            }
        }

        return nums;
    }
}
