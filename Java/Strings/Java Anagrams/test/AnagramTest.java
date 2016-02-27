import org.junit.*;
import static org.junit.Assert.*;

public class AnagramTest {
    @Test
    public void testCase1() {
        assertEquals(Anagram.isAnagram("anagram", "margana"), true);
    }

    @Test
    public void testCase2() {
        assertEquals(Anagram.isAnagram("anagramm", "marganaa"), false);
    }

    @Test
    public void testCase3() {
        assertEquals(Anagram.isAnagram("Hello", "hello"), true);
    }
}
