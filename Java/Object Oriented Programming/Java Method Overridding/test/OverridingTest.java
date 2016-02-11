import org.junit.*;
import static org.junit.Assert.*;
import java.io.*;

public class OverridingTest {
    @Before
    public void setup() {
        System.setOut(new PrintStream(stdout));
    }

    @After
    public void teardown() {
        System.setOut(null);
    }

    @Test
    public void testSoccerIsASport() {
        assertTrue((new Soccer()) instanceof Sports);
    }

    @Test
    public void testSoccerGetName() {
        Soccer soc = new Soccer();
        assertEquals(soc.get_name(), "Soccer Class");
    }

    @Test
    public void testSoccerTeamMembers() {
        Soccer soc = new Soccer();
        String expected = "Each team has 11 players in Soccer Class\n";

        soc.get_number_of_team_members();
        assertEquals(expected, stdout.toString());
    }

    protected final ByteArrayOutputStream stdout = new ByteArrayOutputStream();
}
