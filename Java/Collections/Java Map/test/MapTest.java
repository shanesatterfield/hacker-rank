import org.junit.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class MapTest {
    @Before
    public void setup() {
        sol = new Solution();
    }

    @Test
    public void testCase1() {
        String name   = "uncle sam";
        String number = "99912222";
        testSol(name, number, getFormattedString(name, number));
    }

    @Test
    public void testCase2() {
        String name   = "tom";
        String number = "11122222";
        testSol(name, number, getFormattedString(name, number));
    }

    @Test
    public void testCase3() {
        String name   = "harry";
        String number = "12299933";
        testSol(name, number, getFormattedString(name, number));
    }

    @Test
    public void testFailedRetrieval() {
        String name   = "uncle tom";
        String number = "";
        testGetFormatted(name, "Not found");
    }

    /**
     * Test that inserts a new value into the map and tests that the value can be retrieved properly.
     * @param  The key that will be put into the map.
     * @param  The value that will be put into the map.
     * @param  The string that is expected to be retrieved when calling getFormatted.
     */
    public void testSol(String name, String number, String expected) {
        sol.add(name, number);
        assertEquals(sol.get(name), number);
        testGetFormatted(name, expected);
    }

    /**
     * Tests that the formatted return works properly. No values are put into the map.
     * @param  The key of the object being retrieved.
     * @param  The string that is expected to be retrieved when calling getFormatted.
     */
    public void testGetFormatted(String name, String expected) {
        assertTrue(sol.getFormatted(name).equals(expected));
    }

    /**
     * A helper function that sets up a default string formatting to be checked against in tests.
     * @param   The key of the object that would be retrieved from the map.
     * @param   The value of the object that would be stored in the map.
     * @return  The formatted string containing the key, value pair.
     */
    public String getFormattedString(String name, String number) {
        return String.format("%s=%s", name, number);
    }

    private Solution sol;
}
