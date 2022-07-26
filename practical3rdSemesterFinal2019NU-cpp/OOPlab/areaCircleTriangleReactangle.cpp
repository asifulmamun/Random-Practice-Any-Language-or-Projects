#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double pie = 3.1416;
double result;
double area (int l, int w);
double area (double b, double h);
double area (double r);
double area (int s);

int main() {
	int l,w,s;
	double b,h,r;

	cout<<"Enter the length of rectangle : ";
	cin>>l;
	cout<<"Enter the width of rectangle : ";
	cin>>w;
	area (l,w);

	cout<<"Enter the base of triangle : ";
	cin>>b;
	cout<<"Enter the height of triangle : ";
	cin>>h;
	area (b,h);

	cout<<"Enter the radius of circle : ";
	cin>>r;
	area (r);

	cout<<"Enter the side of square : ";
	cin>>s;
	area (s);
return 0;
}

//Rectangle area
double area(int l, int w){
	result = l*w;
	cout << showpoint;
	cout << fixed;
	cout << setprecision (2);
	cout << "\tThe area of Rectangle is = " << result << endl << endl;
	}

//Triangle area
double area(double b, double h){
	result = (1.0/2)*b*h;
	cout<<"\tThe area of Triangle is = "<<result<<endl<<endl;
	}

//Circle area
double area(double r){
	result = pie*r*r;
	cout<<"\tThe area of Circle is = "<<result<<endl<<endl;
	}

//Square area	
double area(int s){
	result = s*s;
	cout<<"\tThe area of Square is = "<<result<<endl<<endl;
	}