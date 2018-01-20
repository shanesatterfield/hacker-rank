public class Solution {
    public static void main(String args[]) {
        Bird bird = new Bird();
        bird.walk();
        bird.fly();
        bird.sing();
    }
}

class Animal {
    public void walk() {
        System.out.println("I am walking");
    }
}

class Bird extends Animal {
    public void fly() {
        System.out.println("I am flying");
    }

    public void sing() {
        System.out.println("I am singing");
    }
}
