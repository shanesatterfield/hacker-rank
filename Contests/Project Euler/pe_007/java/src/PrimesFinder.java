import java.util.ArrayList;

public class PrimesFinder {
    /**
     * Constructs the new object with the default size for the sieve.
     */
    public PrimesFinder() {
        this(DEFAULT_STARTING_SIZE);
    }

    /**
     * Constructs the new object with the given size for the sieve.
     * @param  startingSize Size of the sieve to calculate primes.
     */
    public PrimesFinder(int startingSize) {
        findPrimes(startingSize);
    }

    /**
     * Get the Nth prime.
     * @param  nth The number of the prime to be retrieved. First, 5th, etc.
     * @return     The Nth prime's value.
     */
    public int getPrime(int nth) {
        if (nth < 1 || nth >= primes.size()) {
            return -1;
        }

        return primes.get(nth - 1);
    }

    /**
     * Finds primes using a sieve and adds them to the list of primes to be retrieved later.
     * @param maxSize The size of the sieve used to find the primes.
     */
    protected void findPrimes(int maxSize) {
        sieve = new Boolean[maxSize];
        if (primes == null) {
            primes = new ArrayList<Integer>();
        }

        // Iterate and do the sieve.
        // Note that primes are false and true values are not primes. This is for optimization.
        for (int i = 0; i < sieve.length; ++i) {
            for (int j = (i*2)+2; j < sieve.length; j += i+2) {
                sieve[j] = true;
            }
        }

        // Collect the primes that were found using the sieve.
        for (int i = 0; i < sieve.length; ++i) {
            if (sieve[i] == null || sieve[i] == false) {
                primes.add(i+2);
            }
        }
    }

    private static final int DEFAULT_STARTING_SIZE = 1000000;
    private ArrayList<Integer> primes;
    private Boolean[] sieve;
}
