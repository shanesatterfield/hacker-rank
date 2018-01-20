import java.io.IOException;
import java.lang.reflect.Method;

class Printer
{
    public <T> void printArray(T[] arr)
    {
        for (int i = 0; i < arr.length; ++i)
        {
            System.out.println(arr[i].toString());
        }
    }
}

public class Solution
{
    public static void main( String args[] )
    {
        // Create the printer object and the Integer and String arrays.
        Printer myPrinter    = new Printer();
        Integer[] intArray   = { 1, 2, 3 };
        String[] stringArray = {"Hello","World"};

        // Print the arrays using the generic print function.
        myPrinter.printArray( intArray  );
        myPrinter.printArray( stringArray );

        // Count the number of functions in the Printer class.
        int count=0;
        for (Method method : Printer.class.getDeclaredMethods()) {
            String name = method.getName();
            if (name.equals("printArray")) {
                count++;
            }
        }

        // Check if there is exactly one function in the object.
        if (count>1) {
            System.out.println("Method overloading is not allowed!");
        }

        assert count == 1;
    }
}

