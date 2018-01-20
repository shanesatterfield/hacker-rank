package hacker;

import java.util.stream.Collectors;
import java.util.Scanner;
import java.util.List;
import java.util.Arrays;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class Application {
    public static List<String> days = Arrays.asList(
        null,
        "SUNDAY",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY"
    );

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        List<Integer> dateData = Arrays.asList(in.next(), in.next(), in.next())
            .stream()
            .map(x -> Integer.parseInt(x))
            .collect(Collectors.toList());

        System.out.println(getDay(dateData.get(0), dateData.get(1), dateData.get(2)));
    }

    public static String getDay(int month, int day, int year) {
        Calendar cal = Calendar.getInstance();
        cal.set(year, month-1, day);
        return days.get(cal.get(Calendar.DAY_OF_WEEK));
    }
}
