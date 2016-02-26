import org.junit.*;
import static org.junit.Assert.*;

public class AnagramTest {
    @Test
    public void testCase1() {
        assertEquals(Anagram.isAnagram("anagram", "margana"), true);
    }

    @Test
    public void testCase1() {
        assertEquals(Anagram.isAnagram("anagramm", "marganaa"), true);
    }
}
