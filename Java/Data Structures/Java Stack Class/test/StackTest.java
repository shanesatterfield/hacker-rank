import org.junit.*;
import static org.junit.Assert.*;

public class StackTest {
    @Test
    public void testCase1() {
        assertTrue(Solution.isBalanced("{}()"));
    }

    @Test
    public void testCase2() {
        assertTrue(Solution.isBalanced("({()})"));
    }

    @Test
    public void testCase3() {
        assertFalse(Solution.isBalanced("{}("));
    }

    @Test
    public void testCase4() {
        assertTrue(Solution.isBalanced("[]"));
    }
}
