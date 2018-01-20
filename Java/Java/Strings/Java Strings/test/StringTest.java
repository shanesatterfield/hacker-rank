import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class StringTest {
    @Test
    public void testCase1() {
        assertThat(Solution.sortSubs("welcometojava", 3), contains("ava", "wel"));
    }
}
