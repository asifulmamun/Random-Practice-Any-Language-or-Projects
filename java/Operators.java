public class Operators{
    public static void main(String[] args) {
        
        // data type declare
        int a, b, sum, sub;

        // data declare
        a = 5;
        b = 10;

        // calculation All Calculation like as python or another system opearator
        sum = a+b;
        sub = b-a;

        System.out.println(Integer.valueOf(String.valueOf(sum) + String.valueOf(sub)));

        System.out.println(sum + " " + sub);
        
        System.out.println(sum + " " + sub);

        System.out.println(String.format("%d, %d", sum, sub));
    }
}