import java.util.*;

/**
 * Solution for Java -> Introduction -> Java Stdin and Stdout.
 * @author Shane Satterfield
 */
class Solution {
    public static void main( String args[] ) {
        // Get a list of the objects from stdin.
        List<Object> ans = getInput();

        // Prints out the input as properly formatted output to stdout.
        System.out.println("String: " + (String)ans.get(2));
        System.out.println("Double: " + (double)ans.get(1));
        System.out.println("Int: "    +    (int)ans.get(0));
    }

    /**
     * Reads input from stdin and returns them as a list of objects.
     * Reads in an int, a double and a String in that order.
     * @return A list of objects corresponding to the data read from stdin.
     */
    public static List<Object> getInput() {
        List<Object> list = new ArrayList<Object>();
        Scanner scan = null;
        try {

            scan = new Scanner(System.in);
            list.add( scan.nextInt() );
            list.add( scan.nextDouble() );
            scan.nextLine();
            list.add( scan.nextLine() );

        } catch( Exception e ) {
            e.printStackTrace();
        } finally {
            if( scan != null ) {
                try { scan.close(); } catch( Exception e ) { e.printStackTrace(); }
            }
        }

        return list;
    }
}
