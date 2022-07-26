#include <iostream>
using namespace std;

// Class Factorial
class factorial {
    public:
        int f;

    factorial (int n) {
        f = 1; // declace initial
        cout << "The factorial of " << n << " is : ";
        
        for (int i = n; i>0; i--) {

            // total of factorial assign
            f *= i;

            // factorial series print
            cout << i;

            // simble
            if (i==1){
                cout<<" = ";
            }
            else{
                cout<<" * ";
            }
        }

        // total factorial result
        cout << f << endl;
    }
};

// Main function
int main(){
    int value;

    // get input number
    cout << "Enter your number : ";
    cin >> value;

    // Factorial Class user interface
    factorial fact(value);

return 0;
}