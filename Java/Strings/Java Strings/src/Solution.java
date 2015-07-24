import java.io.*;
import java.util.*;

/**
 * Prints the smallest and largest lexicographic substring of a specified length.
 * @author Shane Satterfield
 */
class Solution {
    public static void main( String args[] ) {
        BufferedReader br = null;
        try {

            br = new BufferedReader(new InputStreamReader(System.in));
            String word = br.readLine();
            int K = Integer.parseInt(br.readLine());

            List<String> ans = sortSubs(word, K);
            for( String iter: ans ) {
                System.out.println( iter );
            }

        } catch( IOException e ) {
            e.printStackTrace();
        } finally {
            if( br != null ) {
                try {
                    br.close();
                } catch( IOException e ) {
                    e.printStackTrace();
                }
            }
        }

    }

    /**
     * Takes a string and an integer and returns the largest and smallest
     * substring of that length in the string.
     * @param   word    The word to check substrings for.
     * @param   K       The length of the substrings to check for.
     * @return  A list containing two strings. The first string is the minimum
     *            value found and the second is the maximum value found.
     */
    public static List<String> sortSubs( String word, int K ) {
        List<String> sortedList = new ArrayList<String>();
        for( int i = 0; i < word.length() - K + 1; ++i ) {
            sortedList.add(word.substring(i, i+K));
        }
        Collections.sort(sortedList);

        List<String> ans = new ArrayList<String>();
        if( sortedList.isEmpty() == false ) {
            ans.add( sortedList.get(0) );
            ans.add( sortedList.get(sortedList.size()-1) );
        }
        return ans;
    }
}
