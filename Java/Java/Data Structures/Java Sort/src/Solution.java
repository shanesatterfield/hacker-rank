import java.util.*;


/**
 * Solution for Java - Data Structures - Java Sort.
 *
 * You are given a list of student information: ID, FirstName, and CGPA. Your
 * task is to rearrange them according to their CGPA in decreasing order. If
 * two student have the same CGPA, then arrange them according to their first
 * name in alphabetical order. If those two students also have the same first
 * name, then order them according to their ID. No two students have the same
 * ID.
 */
public class Solution {

    public static void main(final String args[]) {

        parseStudents()
            .stream()
            .sorted()
            .forEach(System.out::println);
    }


    public static List<Student> parseStudents() {

        final Scanner in = new Scanner(System.in);
        final int studentCount = Integer.parseInt(in.nextLine());
        final List<Student> students = new ArrayList<Student>(studentCount);

        for (int i = 0; i < studentCount; i++) {

            final int id = in.nextInt();
            final String name = in.next();
            final double cgpa = in.nextDouble();

            students.add(new Student(id, name, cgpa));
        }

        in.close();
        return students;
    }
}


class Student implements Comparable<Student> {

    private final int id;

    private final String fname;

    private final double cgpa;


    public Student(final int id, final String fname, final double cgpa) {
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }


    @Override
    public int compareTo(final Student b) {

        if (cgpa != b.getCgpa()) {
            return cgpa > b.getCgpa() ? -1 : 1;
        }

        else if (fname.compareTo(b.getFname()) != 0) {
            return fname.compareTo(b.getFname());
        }

        else {
            return id - b.getId();
        }
    }

    @Override
    public String toString() {
        return this.getFname();
    }

    public int getId() {
        return id;
    }

    public String getFname() {
        return fname;
    }

    public double getCgpa() {
        return cgpa;
    }
}
