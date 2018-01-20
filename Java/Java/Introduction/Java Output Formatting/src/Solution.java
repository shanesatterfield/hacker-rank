import java.util.*;
import java.io.*;

/**
 * Solution to Java -> Introduction -> Java Output Formatting.
 * @author Shane Satterfield
 */
public class Solution {
    public static void main( String args[] ) {
        PairOutput po = new PairOutput();
        // Reads the input from stdin.
        po.readInput();

        // Outputs the properly formatting data to stdout.
        po.printOutput();
    }
}

class PairOutput {
    public PairOutput() {
        pairs = new ArrayList<Pair>();
    }

    /**
     * Reads the data from stdin as a String and int which are separated
     * by a space character. These pairs are added to the object's list.
     */
    public void readInput() {
        BufferedReader br = null;
        try {

            br = new BufferedReader(new InputStreamReader(System.in));
            String line;
            while( (line = br.readLine()) != null ) {
                String[] parts = line.split(" ");
                addPair(new Pair( parts[0], Integer.parseInt(parts[1]) ));
            }

        } catch( IOException e ) { e.printStackTrace(); }
        finally {
            if( br != null ) {
                try{ br.close(); } catch( IOException e ){ e.printStackTrace(); }
            }
        }
    }

    /**
     * @param newPair Adds this new pair to the list of pairs.
     */
    public void addPair( Pair newPair ) {
        pairs.add( newPair );
    }

    /**
     * Prints all pairs stored in the list with propper formatting.
     */
    public void printOutput() {
        System.out.println("================================");
        for( int i = 0; i < pairs.size(); ++i ) {
            Pair curr = pairs.get( i );
            System.out.printf("%-15s%03d\n", curr.text, curr.num);
        }
        System.out.println("================================");
    }

    protected List<Pair> pairs;
}

/**
 * A pair class that holds both a String and an int value. Used above.
 */
class Pair {
    public Pair( String text, int num ) {
        this.text = text;
        this.num = num;
    }

    public String text;
    public int num;
}
