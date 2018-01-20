import java.util.*;

class Board {
    public Board() {
        board = new ArrayList<>();
    }

    public void addNewRow(Integer[] arr) {
        board.add(Arrays.asList(arr));
    }

    public void addToRow(int row, int item) {
        if (onBoard(row-1, 0)) {
            board.get(row).add(item);
        }
    }

    public int get(int row, int column) throws IndexOutOfBoundsException {
        if (!onBoard(row-1, column)) {
            throw new IndexOutOfBoundsException("The row or column was not found in the board.");
        }

        return board.get(row-1).get(column);
    }

    public boolean onBoard(int row, int column) {
        return row >= 0 && row < board.size() && column >= 0 && column < board.get(row).size();
    }

    protected List<List<Integer>> board;
}

public class Solution {
    public static void main(String args[]) {
        scan  = new Scanner(System.in);
        board = new Board();

        if (!scan.hasNextInt()) {
            return;
        }

        int testCases = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < testCases; ++i) {
            Integer[] nums = splitLine(scan.nextLine());
            board.addNewRow(nums);
        }

        if (!scan.hasNextInt()) {
            return;
        }

        testCases = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < testCases; ++i) {
            String output = "ERROR!";
            try {
                Integer num = board.get(scan.nextInt(), scan.nextInt());
                output = String.valueOf(num);
            }
            catch (IndexOutOfBoundsException e) {}
            finally {
                System.out.println(output);
            }
        }
    }

    public static Integer[] splitLine(String line) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (String num: line.split(" ")) {
            nums.add(Integer.parseInt(num));
        }
        return nums.toArray(new Integer[nums.size()]);
    }

    public static Scanner scan;
    public static Board board;
}
