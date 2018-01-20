import java.util.Scanner;

public class Solution {
    public static void main(String args[]) {
        if (scan.hasNext()) {
            setAndGetTest(scan.nextLine(), new MyBook());
        }
    }

    public static void setAndGetTest(String title, MyBook mybook) {
        mybook.setTitle(title);
        String newTitle = mybook.getTitle();
        System.out.printf("The title is: %s\n", newTitle);
    }

    private static  Scanner scan = new Scanner(System.in);
}

abstract class Book {
    public abstract void setTitle(String newTitle);

    public String getTitle() {
        return title;
    }

    protected String title;
}

class MyBook extends Book {
    public void setTitle(String newTitle) {
        title = newTitle;
    }
}
