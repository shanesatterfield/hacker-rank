import org.junit.*;
import static org.junit.Assert.*;

public class ArrayListTest {
    @Before
    public void setup() {
        board = new Board();
        board.addNewRow(new Integer[]{5, 41, 77, 74, 22, 44});
        board.addNewRow(new Integer[]{1, 12});
        board.addNewRow(new Integer[]{4, 37, 34, 36, 52});
        board.addNewRow(new Integer[]{0});
        board.addNewRow(new Integer[]{3, 20, 22, 33});
    }

    @Test
    public void testCase1() {
        assertEquals(board.get(1, 3), 74);
    }

    @Test
    public void testCase2() {
        assertEquals(board.get(3, 4), 52);
    }

    @Test
    public void testCase3() {
        assertEquals(board.get(3, 1), 37);
    }

    @Test(expected = IndexOutOfBoundsException.class)
    public void testCase4() {
        assertEquals(board.get(4, 3), null);
    }

    @Test(expected = IndexOutOfBoundsException.class)
    public void testCase5() {
        assertEquals(board.get(5, 5), null);
    }

    public Board board;
}
