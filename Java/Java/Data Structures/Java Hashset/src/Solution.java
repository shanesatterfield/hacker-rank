import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Solution {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        Solvent solvent = new Solvent();

        int lineCount = scan.nextInt();

        for (int i = 0; i < lineCount; ++i) {
            solvent.addPair(scan.next(), scan.next());
            System.out.println(solvent.getUniquePairs());
        }
    }
}

// HashSet wrapper
// This can be done with just joining the strings, but this is more robust.
class Solvent {
    private Set<Pair> pairs = new HashSet<>();

    public void addPair(String a, String b) {
        this.pairs.add(new Pair(a, b));
    }

    public int getUniquePairs() {
        return this.pairs.size();
    }
}

// POJO
class Pair {
    public String a;
    public String b;

    public Pair(String a, String b) {
        this.a = a;
        this.b = b;
    }

    public String toString() {
        return String.format("%s,%s", this.a, this.b);
    }

    public boolean equals(Object other) {
        Pair otherPair = (Pair) other;
        return a.equals(otherPair.a) && b.equals(otherPair.b);
    }

    public int hashCode() {
        return this.toString().hashCode();
    }
}
