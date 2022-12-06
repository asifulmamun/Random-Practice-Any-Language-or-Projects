import java.text.DecimalFormat;
import java.util.Scanner; // for input from user

public class Try{
    private static final DecimalFormat df = new DecimalFormat("0.00");

    public static void main(String[] args){

        System.out.println("Enter 2 float number below:");

        double f1;
        double sum;
    
        
        Scanner sc = new Scanner(System.in);
        f1 = sc.nextDouble(); // data type and variable declare before
        double f2 = sc.nextDouble(); // Getting input type declare data type

        sum = f1+f2;
        System.out.println(df.format(sum));
        System.out.printf("Sumi is = %.2f", sum); 

    }

}
