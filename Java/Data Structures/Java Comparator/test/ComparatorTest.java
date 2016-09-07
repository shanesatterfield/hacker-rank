import org.junit.*;
import static org.junit.Assert.*;
import java.util.*;

public class ComparatorTest {
    @Before
    public void setup() {
        check = new Checker();
    }

    @Test
    public void testPlayerAttributes() {
        // Create the player object and the expect values to be inputted into the object.
        Player player = new Player();
        String name   = "John Cena";
        int score     = 100;

        // Store the values into the Player object.
        player.name   = name;
        player.score  = score;

        // Test that the values were inputted properly.
        assertEquals(player.name, name);
        assertEquals(player.score, score);
    }

    @Test
    public void testPlayersSortProperly() {
        // Create the players.
        String[] inputData = new String[] {
            "John Cena",           "100",
            "Bruce Wayne",         "200",
            "Christopher Topher",  "150",
            "Linda Blair",         "6666",
            "Marko Koko",          "12312"
        };

        Player[] players = new Player[(int)(inputData.length/2)];

        for (int i = 0; i < players.length; ++i) {
            players[i]       = new Player();
            players[i].name  = inputData[i*2];
            players[i].score = Integer.parseInt(inputData[i*2+1]);
        }
    }

    private Checker check;
}
