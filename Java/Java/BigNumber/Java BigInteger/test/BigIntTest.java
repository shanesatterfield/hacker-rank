import org.junit.Test;

import static org.hamcrest.MatcherAssert.*;
import static org.hamcrest.Matchers.*;

public class BigIntTest {
    @Test
    public void testCase1() {
        String num1 = "1234";
        String num2 = "20";
        assertThat(Solution.addNums(num1, num2), is(Integer.toString(Integer.parseInt(num1) + Integer.parseInt(num2))));
    }

    @Test
    public void testSmallMultiply() {
        String num1 = "1234";
        String num2 = "20";
        assertThat(Solution.multiplyNums(num1, num2), is(Integer.toString( Integer.parseInt(num1) * Integer.parseInt(num2)) ));

    }
}
