package hacker;

import org.junit.Test;
import static org.junit.Assert.*;

public class ApplicationTest {
    @Test
    public void testCase1() {
        assertEquals(Application.getDay(8, 5, 2015), "WEDNESDAY");
    }

    @Test
    public void testCase2() {
        assertEquals(Application.getDay(12, 25, 2059), "THURSDAY");
    }
}
