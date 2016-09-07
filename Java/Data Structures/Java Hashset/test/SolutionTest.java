import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;

public class SolutionTest {
    private Solvent solvent;

    @Before
    public void setup() {
        solvent = new Solvent();
    }

    @Test
    public void testEmpty() {
        assertEquals(solvent.getUniquePairs(), 0);
    }

    @Test
    public void testOne() {
        solvent.addPair("john", "tom");
        assertEquals(solvent.getUniquePairs(), 1);
    }

    @Test
    public void testTwoSame() {
        solvent.addPair("john", "tom");
        solvent.addPair("john", "tom");
        assertEquals(solvent.getUniquePairs(), 1);
    }

    @Test
    public void testTwoDifferent() {
        solvent.addPair("john", "tom");
        solvent.addPair("john", "mary");
        assertEquals(solvent.getUniquePairs(), 2);
    }

    @Test
    public void testASameBDifferent() {
        solvent.addPair("john", "tom");
        solvent.addPair("john", "mary");
        assertEquals(solvent.getUniquePairs(), 2);
    }

    @Test
    public void testBSameADifferent() {
        solvent.addPair("tom", "john");
        solvent.addPair("mary", "mary");
        assertEquals(solvent.getUniquePairs(), 2);
    }

    @Test
    public void testMultiplePairs() {
        solvent.addPair("john", "tom");
        solvent.addPair("john", "mary");
        solvent.addPair("john", "tom");
        solvent.addPair("mary", "anna");
        solvent.addPair("mary", "anna");
        assertEquals(solvent.getUniquePairs(), 3);
    }
}
