import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrimesTest {
    public void setup() {
        pfind = new PrimesFinder();
    }

    @Test
    public void testCase1() {
        setup();
        assertEquals(pfind.getPrime(3), 5);
    }

    @Test
    public void testCase2() {
        setup();
        assertEquals(pfind.getPrime(6), 13);
    }

    private PrimesFinder pfind;
}
