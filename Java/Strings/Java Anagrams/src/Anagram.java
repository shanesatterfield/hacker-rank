import java.util.*;

class Anagram {
    public Anagram(String anagram) {
        setAnagram(anagram);
    }

    public void setAnagram(String anagram) {
        this.origString = anagram;
        calculateFrequencies();
    }

    public void calculateFrequencies() {
        frequencies = new HashMap<>();
        this.origString.chars().forEach((c) -> {
            char curr = Character.toLowerCase((char)c);
            frequencies.putIfAbsent(curr, 0);
            frequencies.put(curr, frequencies.get(curr) + 1);
        });
    }

    public boolean isAnagram(Anagram b) {
        // Check that the set of letts contained in both anagrams are the same.
        if (this.getLetters().equals(b.getLetters()) == false) {
            return false;
        }

        // Make sure that the frequencies of each letter found are the same.
        for (Character c: this.getLetters()) {
            if (this.get(c) != b.get(c)) {
                return false;
            }
        }

        // If all are the same, then a and b are anagrams of each other.
        return true;
    }

    public int get(char c) {
        return this.frequencies.get(c);
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
