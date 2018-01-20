import java.io.*;
import java.math.BigInteger;

/**
 * Takes two big integers and outputs their sum and products.
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        BufferedReader br = null;
        try {

            br = new BufferedReader(new InputStreamReader(System.in));
            String num1 = br.readLine();
            String num2 = br.readLine();

            System.out.println( addNums(num1, num2) );
            System.out.println( multiplyNums(num1, num2) );

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
     * Takes two strings of arbitrary sizes and addes them together.
     * @param num1 The first string to add.
     * @param num2 The second string to add.
     * @return The sum of the two parameters num1 and num2.
     */
    public static String addNums( String num1, String num2 ) {
        BigInteger a = new BigInteger( num1 );
        BigInteger b = new BigInteger( num2 );

        return a.add(b).toString();
    }

    /**
     * Takes two strings of arbitrary sizes and multiplies them.
     * @param num1 The first string to multiply.
     * @param num2 The second string to multiply.
     * @return The product of the two parameters num1 and num2.
     */
    public static String multiplyNums( String num1, String num2 ) {
        BigInteger a = new BigInteger( num1 );
        BigInteger b = new BigInteger( num2 );

        return a.multiply(b).toString();
    }
}
