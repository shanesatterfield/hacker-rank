# Java Method Overriding

When a subclass inherits a superclass, it can override methods of the superclass. Consider the following Sports class:
```java
class Sports{

   String get_name()
   {
      return "Generic Sports";
   }
   void get_number_of_team_members()
   {
       System.out.println("Each team has n players in "+get_name());
   }
}
```
Now we want to create a Soccer class that inherits the Sports class. We can override the get_name method and return a different string.
```java
class Sports{

   String get_name()
   {
      return "Soccer Class";
   }

}
```
Note that to override a method, the parameters and return type of the new method should be exactly same as the old method.

Your task is simple, you are given a partially completed code in the editor, complete the code so that it prints the following lines:
```
Generic Sports
Each team has n players in Generic Sports
Soccer Class
Each team has 11 players in Soccer Class
```
