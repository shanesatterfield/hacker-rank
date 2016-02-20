import org.junit.*;
import static org.junit.Assert.*;

public class HandshakeTest {
    @Test
    public void testNegative() {
        assertEquals(Solution.handshakes(-1), 0);
    }

    @Test
    public void testZero() {
        assertEquals(Solution.handshakes(0), 0);
    }

    @Test
    public void test1() {
        assertEquals(Solution.handshakes(1), 0);
    }

    @Test
    public void test2() {
        assertEquals(Solution.handshakes(2), 1);
    }

    @Test
    public void test3() {
        assertEquals(Solution.handshakes(3), 3);
    }

    @Test
    public void test4() {
        assertEquals(Solution.handshakes(4), 6);
    }
}
