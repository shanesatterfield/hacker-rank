import java.util.*;

class Sports {
    public String get_name() {
        return "Generic Sports";
    }

    public void get_number_of_team_members() {
        System.out.println("Each team has n players in " + get_name());
    }
}

class Soccer extends Sports {
    public String get_name() {
        return "Soccer Class";
    }

    public void get_number_of_team_members() {
        System.out.println("Each team has 11 players in " + get_name());
    }
}

public class Solution {
       public static void main(String []args) {
            Sports C1=new Sports();
            Soccer C2=new Soccer();
            System.out.println(C1.get_name());
            C1.get_number_of_team_members();
            System.out.println(C2.get_name());
            C2.get_number_of_team_members();
       }
}
