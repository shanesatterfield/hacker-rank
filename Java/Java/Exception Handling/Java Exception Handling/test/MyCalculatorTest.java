import org.junit.Test;

import static org.hamcrest.MatcherAssert.*;
import static org.hamcrest.Matchers.*;

/**
 * Tests the myCalculator class's power function.
 * @author Shane Satterfield
 */
public class MyCalculatorTest {
    @Test
    public void testPowerBothPositive() throws Exception {
        myCalculator mc = new myCalculator();
        assertThat(mc.power(3,5), is(243));
    }

    @Test
    public void testCaseTwo() throws Exception {
        myCalculator mc = new myCalculator();
        assertThat(mc.power(2, 4), is(16));
    }

    @Test(expected=Exception.class)
    public void testPowerBothNegative() throws Exception {
        myCalculator mc = new myCalculator();
        mc.power(-1, -2);
    }

    @Test(expected=Exception.class)
    public void testPowerFirstNegativeOnly() throws Exception {
        myCalculator mc = new myCalculator();
        mc.power(-1, 2);
    }

    @Test(expected=Exception.class)
    public void testPowerSecondNegativeOnly() throws Exception {
        myCalculator mc = new myCalculator();
        mc.power(1, -2);
    }
}
