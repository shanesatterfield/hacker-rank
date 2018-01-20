import java.io.*;
import java.util.*;
import java.math.BigInteger;

/**
 * Take a series of numbers from stdin and outputs which data types those numbers can be placed into
 * without overflowing.
 *
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        BufferedReader br = null;
        try {
            // Create the BufferedReader object to read from stdin.
            br = new BufferedReader(new InputStreamReader(System.in));

            // Retrieve the number of test cases to run through the code.
            int testCases = Integer.parseInt( br.readLine() );

            for( int i = 0; i < testCases; ++i ) {
                // Get the number to check against and run it through the dtypes function to get the answer.
                String num = br.readLine();
                List<String> ans = dtypes(num);

                // Take the answer and print the proper output to stdout.
                if( ans.isEmpty() ) {
                    System.out.printf("%s can't be fitted anywhere.\n", num);
                }
                else {
                    System.out.printf("%s can be fitted in:\n", num);
                    for( int k = 0; k < ans.size(); ++k ) {
                        System.out.printf("* %s\n", ans.get(k));
                    }
                }
            }

        } catch( Exception e ) {
            e.printStackTrace();
        } finally {
            try {
                if( br != null ) {
                    br.close();
                }
            } catch( IOException e ) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determines the Java integer data types that the number snum can be fit into.
     *
     * @param snum The number to check against in String form.
     * @return A list of the names of the data types that snum can be nicely placed into without overflow.
     */
    public static List<String> dtypes( String snum ) {
        // Converts the string number to a Java BigInteger object and retrieves the amount of bits it takes up.
        int bitCount = (new BigInteger(snum)).bitLength() + 1;

        // Logic to determine which is the first data type that the number can fit into.
        int startIndex = 0;
        for( int i = data_types.size()-1; i >= 0; --i ) {
            if( bitCount > data_length.get(i) ) {
                startIndex = i+1;
                break;
            }
        }

        // Returns a sublist containing only the data types that the number can be fit into.
        return data_types.subList(startIndex, data_types.size());
    }

    /** A list containing the string representation of each of the data types. */
    public static List<String> data_types = new ArrayList<String>(){{
        add("byte");
        add("short");
        add("int");
        add("long");
    }};

    /** A list containing the length in bits of each of the data types in the data_types list. */
    public static List<Integer> data_length = new ArrayList<Integer>(){{
        add( 8);
        add(16);
        add(32);
        add(64);
    }};
}
