import org.junit.*;
import static org.junit.Assert.*;

public class ReverseTest {
    @Test
    public void testCase1() {
        assertEquals(Solution.isPalindrome("madam"), true);
    }

    @Test
    public void testCase2() {
        assertEquals(Solution.isPalindrome("anna"), true);
    }

    @Test
    public void testCase3() {
        assertEquals(Solution.isPalindrome("reviver"), true);
    }

    @Test
    public void testCase4() {
        assertEquals(Solution.isPalindrome("things"), false);
    }
}
