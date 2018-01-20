import org.junit.*;
import static org.junit.Assert.*;

public class ReverseGameTest{
    @Test
    public void testCase1() {
        assertEquals(Solution.reverseGame(3, 1), 2);
    }

    @Test
    public void testCase2() {
        assertEquals(Solution.reverseGame(5, 2), 4);
    }

    @Test
    public void testAll9() {
        int[] arr = new int[]{8,0,7,1,6,2,5,3,4};
        for (int i = 0; i < arr.length; ++i) {
            assertEquals(Solution.reverseGame(arr.length, arr[i]), i);
        }
    }
}
