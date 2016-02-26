import java.util.*;

class Anagram {
    public Anagram(String anagram) {
        setAnagram(anagram);
    }

    public void setAnagram(String anagram) {
        this.origString = anagram;
        calculateFrequencies();
    }

    // TODO: Test this funciton.
    public void calculateFrequencies() {
        frequencies = new HashMap<>();
        this.origString.chars().forEach((c) -> {
            frequencies.putIfAbsent((char)c, 0);
            frequencies.put((char)c, frequencies.get(c) + 1);
        });
    }

    // TODO: Finish writing this function.
    public boolean isAnagram(Anagram b) {
        if (this.getLetters().equals(b.getLetters()) == false) {
            return false;
        }
        return true;
    }

    public Set<Character> getLetters() {
        return this.frequencies.keySet();
    }

    public HashMap<Character, Integer> getFrequencies() {
        return frequencies;
    }

    public int getSize() {
        return frequencies.size();
    }

    public static boolean isAnagram(String a, String b) {
        return (new Anagram(a)).isAnagram(new Anagram(b));
    }

    protected String origString;
    protected HashMap<Character, Integer> frequencies;
}

public class AnagramChecker {

}
