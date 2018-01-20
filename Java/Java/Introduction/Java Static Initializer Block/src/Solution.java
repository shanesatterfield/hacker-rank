import java.util.*;

public class Solution {
    public static Scanner scan;
    public static int B;
    public static int H;
    public static boolean flag = true;

    static {
        scan = new Scanner(System.in);
        B    = scan.nextInt();
        H    = scan.nextInt();

        if (B <= 0 || H <= 0) {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }

    // HackerRank test runner code below.
    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }
    }//end of main
}//end of class
