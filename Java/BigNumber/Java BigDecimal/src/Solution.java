import java.util.*;
import java.util.stream.Collectors;
import java.io.*;
import java.math.BigDecimal;

/**
 * Takes a list of decimal values and sorts them in decending order.
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        BufferedReader br = null;
        try {

            br = new BufferedReader(new InputStreamReader(System.in));
            int testCases = Integer.parseInt(br.readLine());

            List<String> nums = new ArrayList<String>();
            for( int i = 0; i < testCases; ++i ) {
                nums.add(br.readLine());
            }

            nums = sortDecimals( nums );

            for( int i = 0; i < nums.size(); ++i ) {
                System.out.println( nums.get(i) );
            }
        } catch( IOException e ) {
            e.printStackTrace();
        } finally {

            if( br != null ) {
                try {
                    br.close();
                } catch( IOException e ) { e.printStackTrace(); }
            }

        }
    }

    /**
     * Takes a list of decimal values as strings and outputs them in decending order.
     * @param nums The list of decimal strings to be sorted.
     * @return A list of decimals in string form.
     */
    public static List<String> sortDecimals( List<String> nums ) {
        // Takes a list of strings and converts it to a list of BigDecimal values.
        List<BigDecimal> decimalList = nums.stream()
            .map(x -> new BigDecimal(x))
            .collect(Collectors.<BigDecimal>toList());

        // Sorts the list and reverses it to put it in descending order.
        Collections.sort( decimalList );
        Collections.reverse( decimalList );

        return decimalList.stream()
            .map(x -> {
                // Converts back to string now that the list is sorted.
                String str = x.toPlainString();

                // This is for formatting.
                double value = x.doubleValue();
                if( Math.abs(value) > 0 && Math.abs(value) < 1 && str.charAt(0) == '0' && str.charAt(1) == '.' ) {
                    str = str.substring(1, str.length());
                }
                return str;
            })
            .collect(Collectors.<String>toList());
    }
}
