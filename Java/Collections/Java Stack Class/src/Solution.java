import java.util.*;

public class Solution {
    public static void main(String args[]) {
        scan = new Scanner(System.in);

        String line = "";
        while (scan.hasNext()) {
            line = scan.nextLine();
            System.out.println(isBalanced(line));
        }
    }

    public static boolean isBalanced(String line) {
        Stack<Character> stack = new Stack<>();
        if (mappings == null) {
            initMappings();
        }

        for (int i = 0; i < line.length(); ++i) {
            if (mappings.containsKey(line.charAt(i))) {
                if (stack.empty() || stack.pop() != mappings.get(line.charAt(i))) {
                    return false;
                }
            }
            else {
                stack.push(line.charAt(i));
            }
        }

        return stack.empty();
    }

    private static void initMappings() {
        mappings = new HashMap<>();
        mappings.put('}','{');
        mappings.put(')','(');
        mappings.put(']','[');
    }

    private static HashMap<Character, Character> mappings;
    private static Scanner scan;
}
