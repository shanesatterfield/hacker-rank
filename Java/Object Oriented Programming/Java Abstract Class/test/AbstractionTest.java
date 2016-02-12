import org.junit.*;
import static org.junit.Assert.*;
import java.io.*;

public class AbstractionTest {
    @Test
    public void testMyBookIsSubclass() {
        MyBook mybook = new MyBook();
        assertTrue(mybook instanceof Book);
    }

    @Test
    public void testSettingTitleWorks() {
        MyBook mybook = new MyBook();
        String newTitle = "This is a new title.";
        mybook.setTitle(newTitle);
        assertEquals(mybook.getTitle(), newTitle);
    }

    @Test
    public void testProperOutput() {
        System.setOut(new PrintStream(stdout));

        // Print to stdout, which is saved in out ByteArrayOutputStream.
        String title = "Hello World";
        Solution.setAndGetTest(title, new MyBook());

        // Check that the output to stdout is correct.
        assertEquals(String.format("The title is: %s\n", title), stdout.toString());

        System.setOut(null);
    }

    private final ByteArrayOutputStream stdout = new ByteArrayOutputStream();
}
