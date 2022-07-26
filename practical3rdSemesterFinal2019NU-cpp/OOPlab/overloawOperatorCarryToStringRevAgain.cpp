#include<iostream>
#include<string.h>

using namespace std;

class STRING {
	char str [1000];
	public:
		void get() {
			cin>>str;
		}
		void print() {
			cout<<str<<endl;
		}
	STRING operator+ (STRING obj) {
		STRING temp;
		char temp_s[1000]="";
		strcat(temp_s,str);
		strcat (temp_s, obj.str);
		strcpy (temp.str, temp_s);
	return temp;
	}

	void operator=(STRING obj) {
		strcpy (str, obj.str);
	}
};

// main
int main() {
	STRING ob1, ob2, ob3, ob4;
	cout<<"first string: ";
	ob1.get();
	cout<<"second string: ";
	ob2.get();
	ob3=ob1+ob2;
	cout<<"concatenation: ";
	ob3.print();
	ob4=ob3; cout<<"copy: ";
	ob4.print();
}