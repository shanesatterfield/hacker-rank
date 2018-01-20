import org.junit.Test;
// import static org.hamcrest.Matchers.*;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

import java.util.*;

public class SolutionTest {
    @Test
    public void testCase1() {
        List<String> ans = Solution.dtypes("-150");
        assertThat(ans, contains("short", "int", "long"));
    }

    @Test
    public void testCase2() {
        List<String> ans = Solution.dtypes("150000");
        assertThat(ans, contains("int", "long"));
    }

    @Test
    public void testCase3() {
        List<String> ans = Solution.dtypes("1500000000");
        assertThat(ans, contains("int", "long"));
    }

    @Test
    public void testCase4() {
        List<String> ans = Solution.dtypes("213333333333333333333333333333333333");
        assertThat(ans, is(empty()));
    }

    @Test
    public void testCase5() {
        List<String> ans = Solution.dtypes("-100000000000000");
        assertThat(ans, contains("long"));
    }
}
