import java.text.DecimalFormat;
import java.util.Scanner; // for input from user

public class Get_input_from_user_then_add_double_number{
    private static final DecimalFormat df = new DecimalFormat("0.00");

    public static void main(String[] args){

        System.out.println("Enter 2 float number below:");

        double f1;
        double sum;
    
        
        try (var sc = new Scanner(System.in)) {
            f1 = sc.nextDouble(); // data type and variable declared before
            double f2 = sc.nextDouble(); // Getting input type declare data type

            sum = f1+f2;
        }
        System.out.println(df.format(sum));
        System.out.printf("Sumi is = %.2f", sum); 

    }

}
