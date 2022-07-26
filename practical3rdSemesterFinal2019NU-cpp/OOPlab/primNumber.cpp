#include <iostream>

using namespace std;


class primNumber{
    public:
        int i, num, isPrime;

    checkPrime(num){
        if(num == 0 ){
            cout << "0 is not prime number.";
        }

        else if(num == 1){
            cout << "1 is not prime number.";
        }
        
        for(i=2; i<num; i++){
            if(num%i == 0){
                isPrime = 0;
            }
        }


        if(isPrime > 0){
            cout << num << " is prime number.";
        }
        else{
            cout << num << " is not prime number.";
        }
    }
};

int main(){ 
    int num;
    cout << "Enter Any Number for check prime or not: ";
    cin >> num;

    checkPrime (num);

return 0;
}