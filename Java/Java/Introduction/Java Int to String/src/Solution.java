import java.util.*;
import java.security.*;
public class Solution {
    public static void main(String[] args) {

        Do_Not_Terminate.forbidExit();

        try{
            Scanner in = new Scanner(System.in);
            int n      = in.nextInt();
            String s   = String.valueOf(n);

            if (n == Integer.parseInt(s)) {
                System.out.println("Good job.");
            }
            else {
                System.out.println("Wrong answer.");
            }
        }
        catch (Do_Not_Terminate.ExitTrappedException e) {
            System.out.println("Unsuccessful Termination!!");
        }
    }
}

class Do_Not_Terminate {
    public static class ExitTrappedException extends SecurityException {
        private static final long serialVersionUID = 1L;
    }

    public static void forbidExit() {
        final SecurityManager securityManager = new SecurityManager() {
            @Override
            public void checkPermission(Permission permission) {
                if (permission.getName().contains("exitVM")) {
                    throw new ExitTrappedException();
                }
            }
        };
        System.setSecurityManager(securityManager);
    }
}
