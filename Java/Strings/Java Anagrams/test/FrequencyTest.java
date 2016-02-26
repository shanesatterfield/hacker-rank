import org.junit.*;
import static org.junit.Assert.*;

public class FrequencyTest {
    @Test
    public void testFrequencyFinderZero() {
        Anagram ana = new Anagram("");
        assertEquals(ana.size(), 0);
    }

    @Test
    public void testFrequencyOne() {
        Anagram ana = new Anagram('a');
        assertEquals(ana.getSize(), 1);
        assertEquals(ana.get('a'), 1);
    }

    @Test
    public void testFrequencyOneEach() {
        String anagram = "abcdefghlmnopqrstuvwxyz";
        Anagram ana = new Anagram(anagram);
        assertEquals(ana.getSize(), 26);
        for (Character c: anagram) {
            assertEquals(ana.get(c), 1);
        }
    }

    @Test
    public void testCaseInsensitiveStoring() {
        String anagram = "asdf";
        Anagram ana = new Anagram(anagram);
        assertEquals(ana.getSize(), 4);
        for (Character c: anagram) {
            // Make sure to find the lower case character.
            assertTrue(ana.containsKey(toLower(c)));

            // Make sure not to find the upper case character.
            assertFalse(ana.containsKey(c));
        }
    }

    @Test
    public void testMultiples() {
        String anagram = "whatwhat";
        Anagram ana = new Anagram(anagram);

        assertEquals(ana.getSize(), 8);
        for (Character c: anagram) {
            // Test that the frequencies are 2.
        }
    }

    public static char toLower(char c) {
        if (c >= 'A' && c <= 'Z') {
            return (char)(c+32);
        }
        return c;
    }
}
