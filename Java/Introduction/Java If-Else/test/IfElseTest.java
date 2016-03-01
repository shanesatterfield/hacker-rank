import org.junit.*;
import static org.junit.Assert.*;

public class IfElseTest {
    @Test
    public void testCase1() {
        testRange(1, 100, "Weird");
    }

    @Test
    public void testNotWeird() {
        testRange(2, 5, "Not Weird");
    }

    @Test
    public void testMiddleClass() {
        testRange(6, 20, "Weird");
    }

    @Test
    public void testOnePercent() {
        for (int i = 20; i > 20 && i <= 100; ++i) {
            assertEquals(Solution.diamond(i), "Not Weird");
        }
    }

    public void testRange(int start, int stop, String value) {
        for (int i = start; i <= stop; i += 2) {
            assertEquals(Solution.diamond(i), value);
        }
    }
}
