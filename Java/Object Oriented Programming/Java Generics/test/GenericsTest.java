import org.junit.*;
import static org.junit.Assert.*;
import java.io.*;

public class GenericsTest {
    @Before
    public void setup() {
        System.setOut(new PrintStream(stdout));
        printer = new Printer();
    }

    @After
    public void teardown() {
        System.setOut(null);
    }

    @Test
    public void testPrintIntegers() {
        // Setup the integer array that is to be printed and checked.
        Integer[] arr = {1, 2, 3};
        String expected = joinArray(arr);

        // Print and test the output.
        printer.printArray(arr);
        assertEquals(expected, stdout.toString());
    }

    @Test
    public void testPrintString() {
        // Setup the array to be printed and the expected string value to be checked against.
        String[] arr = {"Hello", "World"};
        String expected = joinArray(arr);

        // Print the values using the generic print function.
        printer.printArray(arr);

        // Assert that the printed values are the ones that were expected.
        assertEquals(expected, stdout.toString());
    }

    /**
     * Helper function for joining an array into a string with a newline separator and one at the end.
     * @param  arr The array that is to be joined.
     * @return     The resulting string of the join.
     */
    protected <T> String joinArray(T[] arr) {
        String result = "";
        for (int i = 0; i < arr.length; ++i) {
            result += arr[i].toString() + "\n";
        }
        return result;
    }

    private Printer printer;
    private final ByteArrayOutputStream stdout = new ByteArrayOutputStream();
}
