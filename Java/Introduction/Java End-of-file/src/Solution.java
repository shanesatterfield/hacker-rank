import java.io.*;

/**
 * Reads from stdin until EOF is reached.
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        BufferedReader br = null;
        try {
            br = new BufferedReader(new InputStreamReader(System.in));
            int lineNumber = 0;
            String line = br.readLine();

            while( line != null ) {
                System.out.printf("%d %s\n", ++lineNumber, line);
                line = br.readLine();
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
}
