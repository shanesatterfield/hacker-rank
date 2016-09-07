import java.util.Scanner;
import java.util.HashMap;

public class Solution {

    private Scanner scan;
    private HashMap<String, String> phoneMap;

    public Solution() {
        scan     = new Scanner(System.in);
        phoneMap = new HashMap<String, String>();
    }

    public void run() {
        if (scan.hasNextInt()) {
            int numTestCases = scan.nextInt();
            scan.nextLine();
            addFromStdin(numTestCases);
        }

        while (scan.hasNextLine()) {
            String name   = scan.nextLine();
            System.out.println(getFormatted(name));
        }
    }

    public void addFromStdin(int numTestCases) {
        String key;
        String value;

        for (int i = 0; i < numTestCases; ++i) {
            key   = scan.nextLine();
            value = scan.nextLine();
            this.add(key, value);
        }
    }

    public void add(String name, String number) {
        phoneMap.put(name, number);
    }

    public String get(String name) {
        return phoneMap.get(name);
    }

    public String getFormatted(String name) {
        String number = this.get(name);
        String output = "Not found";

        if (number != null) {
             output = String.format("%s=%s", name, number);
        }

        return output;
    }

    public static void main(String args[]) {
        Solution sol = new Solution();
        sol.run();
    }
}
