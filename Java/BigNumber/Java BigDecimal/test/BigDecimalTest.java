import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

import java.util.*;

public class BigDecimalTest {
    @Test
    public void testSpitBackList() {
        List<String> nums = new ArrayList<String>();
        nums.add("50.6");
        assertThat(Solution.sortDecimals(nums), contains(nums.get(0)));
    }

    @Test
    public void testCase1() {
        List<String> nums = new ArrayList<String>();
        nums.add("-100");
        nums.add("50");
        nums.add("0");
        nums.add("56.6");
        nums.add("90");

        assertThat(Solution.sortDecimals(nums), contains("90", "56.6", "50", "0", "-100"));
    }
}
