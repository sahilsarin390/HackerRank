import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int myInt = input.nextInt();
        double myDouble = input.nextDouble();
        input.nextLine();
        String myString = input.nextLine();
        input.close();

        System.out.println("String:" + " " + myString);
        System.out.println("Double:" + " " + myDouble);
        System.out.println("Int:" + " " + myInt);
    }
}
