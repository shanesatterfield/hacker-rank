import org.junit.*;
import static org.junit.Assert.*;

public class FrequencyTest {
    @Test
    public void testFrequencyFinderZero() {
        Anagram ana = new Anagram("");
        assertEquals(ana.getSize(), 0);
    }

    @Test
    public void testFrequencyOne() {
        Anagram ana = new Anagram("a");
        assertEquals(ana.getSize(), 1);
        assertEquals(ana.get('a'), 1);
    }

    @Test
    public void testFrequencyOneEach() {
        String anagram = "abcdefghijklmnopqrstuvwxyz ";
        Anagram ana = new Anagram(anagram);

        // Check that there are the right number of letters found.
        assertEquals(ana.getSize(), 27);

        // Check that each letter appeared only once.
        anagram.chars().forEach((c) -> {
            assertEquals(ana.get((char)c), 1);
        });
    }

    @Test
    public void testCaseInsensitiveStoring() {
        String anagram = "asdf";
        Anagram ana = new Anagram(anagram);

        assertEquals(ana.getSize(), 4);
        anagram.chars().forEach((c) -> {
            // Make sure to find the lower case character.
            assertTrue(ana.getFrequencies().containsKey(toLower((char)c)));

            // Make sure not to find the upper case character.
            assertFalse(ana.getFrequencies().containsKey(c));
        });
    }

    @Test
    public void testMultiples() {
        String anagram = "whatwhat";
        Anagram ana = new Anagram(anagram);

        assertEquals(ana.getSize(), 4);
        anagram.chars().forEach((c) -> {
            // Test that the frequencies are 2.
            assertEquals(ana.get((char)c), 2);
        });
    }

    public static char toLower(char c) {
        if (c >= 'A' && c <= 'Z') {
            return (char)(c+32);
        }
        return c;
    }
}
