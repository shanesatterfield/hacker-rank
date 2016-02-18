import org.junit.*;
import static org.junit.Assert.*;

public class RestaurantTest {
    @Test
    public void testCase1() {
        assertEquals(Solution.getSlices(38,   751),  28538);
        assertEquals(Solution.getSlices(344,  734),  63124);
        assertEquals(Solution.getSlices(165,  635),  4191);
        assertEquals(Solution.getSlices(297,  667),  198099);
        assertEquals(Solution.getSlices(917,  264),  242088);
        assertEquals(Solution.getSlices(544,  642),  87312);
        assertEquals(Solution.getSlices(254,  914),  58039);
        assertEquals(Solution.getSlices(612,  50),   7650);
        assertEquals(Solution.getSlices(94,   707),  66458);
        assertEquals(Solution.getSlices(564,  417),  26132);
        assertEquals(Solution.getSlices(145,  246),  35670);
    }

    @Test
    public void testTCase2() {
        assertEquals(Solution.getSlices(309,  528),  18128);
        assertEquals(Solution.getSlices(577,  101),  58277);
        assertEquals(Solution.getSlices(371,  314),  116494);
        assertEquals(Solution.getSlices(207,  346),  71622);
        assertEquals(Solution.getSlices(284,  715),  203060);
        assertEquals(Solution.getSlices(178,  791),  140798);
        assertEquals(Solution.getSlices(725,  295),  8555);
        assertEquals(Solution.getSlices(796,  916),  45571);
        assertEquals(Solution.getSlices(667,  231),  154077);
        assertEquals(Solution.getSlices(282,  302),  21291);
        assertEquals(Solution.getSlices(984,  882),  24108);
        assertEquals(Solution.getSlices(718,  844),  151498);
        assertEquals(Solution.getSlices(372,  749),  278628);
        assertEquals(Solution.getSlices(735,  419),  307965);
        assertEquals(Solution.getSlices(979,  914),  894806);
        assertEquals(Solution.getSlices(444,  837),  41292);
        assertEquals(Solution.getSlices(715,  67),   47905);
        assertEquals(Solution.getSlices(381,  22),   8382);
        assertEquals(Solution.getSlices(367,  87),   31929);
        assertEquals(Solution.getSlices(801,  365),  292365);
        assertEquals(Solution.getSlices(157,  429),  67353);
        assertEquals(Solution.getSlices(723,  756),  60732);
        assertEquals(Solution.getSlices(673,  882),  593586);
        assertEquals(Solution.getSlices(890,  520),  4628);
        assertEquals(Solution.getSlices(599,  342),  204858);
    }

    @Test
    public void testCase3() {
        assertEquals(Solution.getSlices(2, 2), 1);
        assertEquals(Solution.getSlices(6, 9), 6);
    }
}
