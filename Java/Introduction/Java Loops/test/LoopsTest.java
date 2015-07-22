import org.junit.Test;
import java.util.*;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class LoopsTest {
    @Test
    public void testCase1() {
        assertThat(Solution.genAnsList(new int[]{ 0, 2, 10 }), contains(2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046));
    }

    @Test
    public void testCase2() {
        assertThat(Solution.genAnsList(new int[]{ 5, 3, 5 }), contains(8, 14, 26, 50, 98));
    }

    @Test
    public void testCase3() {
        assertThat(Solution.genAnsList(new int[]{ 3, 3, 3 }), contains(6, 12, 24));
    }

    @Test
    public void testCase4() {
        assertThat(Solution.genAnsList(new int[]{ 0, 0, 5 }), contains(0, 0, 0, 0, 0));
    }

    @Test
    public void testCase5() {
        assertThat(Solution.genAnsList(new int[]{ 6, 6, 10 }), contains(12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144));
    }
}
