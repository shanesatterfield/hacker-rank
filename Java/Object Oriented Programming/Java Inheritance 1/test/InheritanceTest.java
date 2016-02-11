import org.junit.*;
import static org.junit.Assert.*;
import java.io.*;

public class InheritanceTest {
    @Before
    public void setup() {
        System.setOut(new PrintStream(stdout));
    }

    @After
    public void teardown() {
        System.setOut(null);
    }

    @Test
    public void testBirdIsAnimal() {
        Bird bird = new Bird();
        assertTrue(bird instanceof Animal);
    }

    @Test
    public void testAnimalWalk() {
        Animal animal = new Animal();
        animal.walk();
        assertEquals("I am walking\n", stdout.toString());
    }

    @Test
    public void testBirdWalkingIsSame() {
        // Find the animals in the wild.
        Animal animal = new Animal();
        Bird bird = new Bird();

        // Observe the way they walk.
        animal.walk();
        bird.walk();

        // If they walk the same, maybe they are the same.
        String[] actual = stdout.toString().split("\n");
        assertEquals(actual[0], actual[1]);

    }

    @Test
    public void testBirdFlies() {
        Bird bird = new Bird();
        bird.fly();
        assertEquals("I am flying\n", stdout.toString());
    }

    @Test
    public void testBirdSings() {
        Bird bird = new Bird();
        bird.sing();
        assertEquals("I am singing\n", stdout.toString());
    }

    public final ByteArrayOutputStream stdout = new ByteArrayOutputStream();
}
