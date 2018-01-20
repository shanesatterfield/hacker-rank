import java.util.List;
import java.util.LinkedList;

import java.util.stream.Stream;
import java.math.BigInteger;
import java.util.stream.IntStream;

import java.util.Arrays;
import org.junit.Test;
import static org.junit.Assert.*;

public class ApplicationTest {
    @Test
    public void testPrime() {
        Arrays.asList(2, 3, 5, 7, 11, 13, 47)
            .stream()
            .map(x -> Integer.valueOf(x))
            .map(x -> BigInteger.valueOf(x))
            .forEach(x -> assertTrue(Application.isPrime(x)));
    }

    @Test
    public void testNotPrirme() {
        IntStream
            .iterate(4, i -> i + 2)
            .limit(100)
            .map(x -> Integer.valueOf(x))
            .mapToObj(x -> BigInteger.valueOf(x))
            .forEach(x -> assertFalse(Application.isPrime(x)));
    }
}
