import java.util.*;

class Student {}
class Rockstar {}
class Hacker {}

public class Solution {
    static String count(ArrayList mylist) {
        int a = 0;
        int b = 0;
        int c = 0;

        for (int i = 0; i < mylist.size(); ++i) {
            Object elem = mylist.get(i);
            if (elem instanceof Student) {
                a++;
            }
            else if (elem instanceof Rockstar) {
                b++;
            }
            else if (elem instanceof Hacker) {
                c++;
            }

        }

        String ret = String.format("%d %d %d", a, b, c);
        return ret;
    }

    public static void main(String args[]) {
        ArrayList mylist = new ArrayList();
        Scanner scan = new Scanner(System.in);

        int t = scan.nextInt();
        for (int i = 0; i < t; ++i) {
            String s = scan.next();
            if (s.equals("Student")) {
                mylist.add(new Student());
            }
            else if (s.equals("Rockstar")) {
                mylist.add(new Rockstar());
            }
            else if (s.equals("Hacker")) {
                mylist.add(new Hacker());
            }

        }

        System.out.println(count(mylist));
    }
}
