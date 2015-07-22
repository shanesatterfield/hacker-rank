import java.util.*;

/**
 * A class used below that calculates exponentials and throws an exception on
 * negative inputs.
 */
class myCalculator {
    /**
     * Calculates exponentials and throws exceptions on negative inputs.
     * @param   n The base number.
     * @param   p The exponent.
     * @return  The exponential n^p or an exception.
     */
    public int power( int n, int p ) throws Exception {
        if( n < 0 || p < 0 ) {
            throw new Exception("n and p should be non-negative");
        }
        return (int)(Math.pow( n, p ));
    }
}

// Code below is supplied by HackerRank.
class Solution{

    public static void main(String []argh)
    {
        Scanner in = new Scanner(System.in);

        while(in.hasNextInt())
        {
            int n = in.nextInt();
            int p = in.nextInt();
            myCalculator M = new myCalculator();
            try
            {
                System.out.println(M.power(n,p));
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }

    }
}
