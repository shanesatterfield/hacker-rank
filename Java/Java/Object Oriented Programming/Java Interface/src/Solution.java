import java.util.*;
interface AdvancedArithmetic{
  public abstract int divisorSum(int n);
}

/**
 * A class that implements the AdvancedArithmetic interface.
 * @author Shane Satterfield
 */
class MyCalculator implements AdvancedArithmetic {
    /**
     * Takes an integer and returns the sum of its divisors.
     * @param  n The number to get and sum the divisors from.
     * @return   The sum of the divisors of the parameter.
     */
    public int divisorSum( int n ) {
        List<Integer> nums = new ArrayList<Integer>();
        for( int i = 1; i <= n; ++i ) {
            if( n % i == 0 ) {
                nums.add( i );
            }
        }

        int total = 0;
        for( int iter: nums ) {
            total += iter;
        }
        return total;
    }
}

class Solution{

    public static void main(String []argh)
    {
        MyCalculator my_calculator=new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.print(my_calculator.divisorSum(n)+"\n");

    }
    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o)
    {

        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++)
        {
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}
