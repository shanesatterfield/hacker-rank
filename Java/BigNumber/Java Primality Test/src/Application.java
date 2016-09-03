import java.util.Scanner;
import java.math.BigInteger;

public class Application {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        BigInteger num = scan.nextBigInteger();
        scan.close();

        String msg = (Application.isPrime(num) ? "prime" : "not prime");
        System.out.println(msg);
    }

    public static boolean isPrime(BigInteger num) {
        return num.isProbablePrime(1000);
    }
}
